# bajaj_finserv
 Smart India Hackathon 

## 1. Create and activate a virtual environment
    python -m venv env
    source env/bin/activate

## 2. Install dependencies
    pip install django
    pip install djangorestframework

## 3. Migrate any changed made to the APIs 
    python manage.py makemigrations accounts
    python manage.py migrate

## 4. Run the django server
    python manage.py runserver
    
