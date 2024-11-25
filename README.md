# Django Hello World App

This is a simple Django app with two routes:
1. A **JSON response** that returns `{"Message": "Hello World!"}`.
2. An **HTML page** styled with a beige background that displays "Hello World!" in bold.

## Features
- JSON Response: Accessible at `http://127.0.0.1:8000/json/`
- HTML Page: Accessible at `http://127.0.0.1:8000/html/`
- Root URL (`/`) redirects to the HTML page.

## Prerequisites
- Python 3.x
- Django 5.x

## How to Run the Project
1. Clone the repository:
   git clone <your-repository-url>
   cd django_helloworld
2.Create a virtual environment:
  python3 -m venv myenv
  source myenv/bin/activate
3.Install dependencies:
  pip install django
4.Run migrations:
  python manage.py migrate
5.Start the development server:
  python manage.py runserver
6.Access the app in your browser:

JSON Response: http://127.0.0.1:8000/json/
HTML Page: http://127.0.0.1:8000/html/
Root URL: http://127.0.0.1:8000/



