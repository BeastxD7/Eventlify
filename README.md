
# Eventlify

Eventlify is a Django-powered web application that allows users to browse, register for, and manage events. It includes features like event registration, organizer dashboard, and a developer showcase page. Deployed on PythonAnywhere, it’s accessible to the public for event management and exploration.

## Features

- **Event Registration**: Users can register for events with ease.
- **Organizer Dashboard**: Hosts can create, edit, and delete events.
- **Developer Page**: Showcases developers who contributed to the project.
- **UI Enhancements**: Friendly confirmation modals and responsive design.

## Deployment

You can view the live project here: [Eventlify on PythonAnywhere](https://shashankdevadiga.pythonanywhere.com/)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Eventlify.git
   cd Eventlify
   ```

2. **Install Dependencies**:
   Ensure you have `pip` and `virtualenv` installed, then create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

## Usage

- **Access the Admin Dashboard**: Register or log in to manage your events.
- **Developers Page**: View contributing developers directly on the site.
