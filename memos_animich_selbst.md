# Setup django

## Step 1: Set up your environment
- python -m venv myenv

- myenv\Scripts\activate

- pip install django

## Step 2: Create a new Django project
cd components/django
- django-admin startproject mysite

##  Step 3: Run the development server
- cd components/django/mysite

- python manage.py runserver

- http://127.0.0.1:8000/

## Step 4: Create a Django app

python manage.py startapp hello

## Step 5: Add the app to the project
````py
# mysite/settings.py
INSTALLED_APPS = [
    # other apps...
    'hello',
]
````
## Step 6: Create a simple view
````py
# hello/views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

````
## Step 7: Define a URL for the view
urls.py file im Ordner hello erstellen
````py
# hello/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
]
````
Nun eine urls.py im Ordner mysite
````py
# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),  # Include the hello app's URLs
]

````
## Step 8: Run the server

- python manage.py runserver

Visit  
http://127.0.0.1:8000/  

and you should see the message "Hello, World!"

## Step 9: Optional - Explore the admin interface

- python manage.py createsuperuser

1. Follow the prompts to create a username and password.
2. Then, visit  

 http://127.0.0.1:8000/admin/ 
 
 and log in with the superuser credentials.
