from django.urls import path
from gameTickets import views

urlpatterns = [
    path('', views.index, name='index')
]