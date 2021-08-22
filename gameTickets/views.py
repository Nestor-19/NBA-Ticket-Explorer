from django.shortcuts import render
import json
from SlamDunkHacks.settings import BASE_DIR
# Create your views here.


def index(request):
    return render(request, 'index.html')


def dashboard(request):

    json_data = open(BASE_DIR / 'static' / 'CrawledData' / 'logos.json')
    data = json.load(json_data)
    return render(request, 'dashboard.html', {"teams": data})


def tickets(request):
    return render(request, 'tickets.html')


def tkt(request, team_name):
    return render(request, 'tkt.html', {"name": team_name})
