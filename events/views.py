from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .forms import CustomUserCreationForm, EventRegistrationForm 
from .models import Event,Registration
from datetime import datetime


# Homepage view
def homepage(request):
    return render(request, 'events/homepage.html', {'current_year': datetime.now().year})

# Login view
def login_user(request):
    return render(request, 'events/login.html')

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Add a success message
            messages.success(request, 'Registration successful! You can now log in.')
            # Redirect to the homepage or login page
            return redirect('login')  # Or 'homepage' if you prefer
    else:
        form = CustomUserCreationForm()
    return render(request, 'events/register.html', {'form': form})



# Event list view
def event_list(request):
    # Fetch all events from the database
    events = Event.objects.all()
    
    # Pass the events to the template
    return render(request, 'events/event_list.html', {'events': events})

# Event details view
def event_details(request, eventname):
    # Fetch the event by its name or slug. Use get_object_or_404 to handle cases where the event does not exist.
    event = get_object_or_404(Event, name=eventname)  # Change 'name' to the appropriate field if using a slug or ID

    return render(request, 'events/event_details.html', {'event': event})

# Event creation form view
@login_required
def event_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        category = request.POST.get('category')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        # Create the event object and set the organizer to the current user
        event = Event(
            name=name,
            description=description,
            date=date,
            time=time,
            location=location,
            category=category,
            price=price,
            image=image,
            organizer=request.user  # Set the organizer
        )
        event.save()

        return redirect('event_list')  # Redirect to the event list or any other page

    return render(request, 'events/event_create.html')


# Event registration view
@login_required
def event_register(request, eventname): 
    event = get_object_or_404(Event, name=eventname)
    
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            # Assuming you have a Registration model
            Registration.objects.create(
                user=request.user,
                event=event,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                contact=form.cleaned_data['contact'],
            )
            return redirect('event_details', eventname=eventname)  # Redirect after successful registration
    else:
        form = EventRegistrationForm()

    return render(request, 'events/event_register.html', {'event': event, 'form': form})


@login_required
def event_register(request, eventname):
    event = get_object_or_404(Event, name=eventname)
    
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)

        # Check if the user is already registered
        if Registration.objects.filter(user=request.user, event=event).exists():
            return render(request, 'events/info.html', {
                'message': 'You are already registered for this event.',
                'message_type': 'error'
            })
        
        if form.is_valid():
            # Create a Registration instance
            Registration.objects.create(
                user=request.user,
                event=event,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                contact=form.cleaned_data['contact'],
            )
            return render(request, 'events/info.html', {
                'message': 'You have successfully registered for the event!',
                'message_type': 'success'
            })
    else:
        form = EventRegistrationForm()

    return render(request, 'events/event_register.html', {'event': event, 'form': form})


@login_required
def dashboard(request):
    registrations = Registration.objects.filter(user=request.user)
    return render(request, 'events/dashboard.html', {'registrations': registrations})


@login_required
def event_dashboard(request):
    # Get events hosted by the logged-in user
    hosted_events = Event.objects.filter(organizer=request.user)
    return render(request, 'events/event_dashboard.html', {'hosted_events': hosted_events})


@login_required
def event_stats(request, eventname):
    # Get the specific event and its registrations
    event = Event.objects.get(name=eventname, organizer=request.user)
    registrations = Registration.objects.filter(event=event)
    return render(request, 'events/event_stats.html', {'event': event, 'registrations': registrations})


@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.organizer == request.user:
        event.delete()
        messages.success(request, "Event deleted successfully.")
        return redirect('event_dashboard')
    else:
        messages.error(request, "You are not authorized to delete this event.")
        return redirect('event_dashboard')
    
def developer_page(request):
    return render(request, 'events/developers.html')