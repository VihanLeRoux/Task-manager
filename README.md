# Task Manager

A simple task management application built with Django that allows users to create, manage, and track tasks.

## Features

- Create, update, and delete tasks
- Mark tasks as complete or incomplete
- Filter tasks by status (all, completed, pending)
- Responsive design

## Technologies Used

- Django
- Python
- SQLite (or any other database you are using)
- HTML, CSS, JavaScript

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/VihanLeRoux/Task-manager.git
   cd Task-manager

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows use: venv\Scripts\activate

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt

4. **Apply migrations:**

   ```bash
   python manage.py migrate

5. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
 
6. **Run the development server:**

   ```bash
   python manage.py runserver

7. **Access the application:**
   
   Open your web browser and go to http://127.0.0.1:8000.

