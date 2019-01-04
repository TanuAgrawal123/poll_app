# poll app website using Django framework
A simple poll app web app.
## Getting started with development
Dependencies:

- Python 3.6.x
- Django 1.11.x

### 1. Clone this repository 
```commandline
git clone https:\\github.com\TanuAgrawal123\poll_app
```

### 2. Install and activate the virtual environment for Windows 
```commandline
python3 -m venv myvenv
myvenv\scripts\activate
```

### 3. Install python packages
```commandline
pip install -r requirements.txt
```

### 4. Run database migrations
```commandline
python manage.py migrate
```

### 5. Create superuser
```commandline
python manage.py createsuperuser
```

### 6. Run development server 
```commandline
python manage.py runserver
```