# Expense_Income Tracker API

A RESTful API for tracking personal expenses and incomes with JWT authentication.

## Features

- ✅ User registration & login
- 🔐 JWT authentication
- 💰 Expense/income tracking
- 🧮 Automatic tax calculations
- 📊 Paginated responses
- 👤 User-specific data isolation
- 👑 Admin access to all records

## Technologies

- Python 3.8+
- Django 4.0+
- Django REST Framework
- SimpleJWT (JSON Web Tokens)
- SQLite (Development)

## Setup
1. Clone repository
   
   git clone https://github.com/Mehulrawat/exp_inc_tracker.git
   cd exp_inc_tracker

2. Create virtual environment
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows

3. Install dependencies:
    pip install -r requirements.txt


4.	Configure database:
    python manage.py migrate

5.	Create superuser
	python manage.py createsuperuser
   
7.	Run the development server
    python manage.py runserver



