from django.urls import path
from gameTickets import views

app_name = 'gameTickets'
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('tickets/<str:team_name>', views.tickets, name='tickets'),
    # path('tickets/<str:team_name>', views.tkt, name='tkt')
]
