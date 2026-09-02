from django.urls import path
from tablero import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
