from django.urls import path
from . import views
#This will route our request to the front end view

urlpatterns = [
	path('', views.index, name="Frontend"),
]