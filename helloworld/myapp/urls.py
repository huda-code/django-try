from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world_html, name='home'),  # Root URL now points to the HTML response
    path('html/', views.hello_world_html, name='hello_world_html'),
    path('json/', views.hello_world_json, name='hello_world_json'),
]
