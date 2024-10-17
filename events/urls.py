from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', auth_views.LoginView.as_view(template_name='events/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='homepage'), name='logout'),
    path('register/', views.register_user, name='register'),
    path('events/', views.event_list, name='event_list'),
    path('event-details/<str:eventname>/', views.event_details, name='event_details'),
    path('event-create/', views.event_create, name='event_create'),
    path('event-register/<str:eventname>/', views.event_register, name='event_register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
