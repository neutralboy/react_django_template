from django.urls import path
from . import views
urlpatterns = [
	path('user_data/', views.current_user_data, name="current_user_data"),
]