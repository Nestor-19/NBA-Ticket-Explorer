from django.shortcuts import render
import json
from SlamDunkHacks.settings import BASE_DIR
from .getJsonData import getCoverPage
# Create your views here.


def index(request):
    return render(request, 'index.html')


def dashboard(request):

    json_data = open(BASE_DIR / 'static' / 'CrawledData' / 'logos.json')
    data = json.load(json_data)
    return render(request, 'dashboard.html', {"teams": data})


def tickets(request, team_name):
    coverImageUrl = getCoverPage(team_name)
    return render(request, 'tickets.html', {"name": team_name, "coverImg": coverImageUrl})
