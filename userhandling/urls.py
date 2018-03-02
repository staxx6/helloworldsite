from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.show_user, name="show_user"),
    path('registration', views.user_registration, name="user_registration"),
]
