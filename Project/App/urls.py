from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="foodFitness"),
    path('newUser/', views.newUser, name="newUser"),
]