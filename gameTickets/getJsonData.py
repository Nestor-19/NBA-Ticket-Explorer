import json
from SlamDunkHacks.settings import BASE_DIR


def getCoverPage(team_name):
    json_data = open(BASE_DIR / 'static' / 'CrawledData' / 'cover.json')
    data = json.load(json_data)

    return data[team_name]


def getAllDates(team_name):
    SH = json.load(open(BASE_DIR / 'static' / 'CrawledData' /
                   'stubHubNew.json'))[team_name].keys()
    TP = json.load(open(BASE_DIR / 'static' / 'CrawledData' /
                   'tickpickNew.json'))[team_name].keys()
    GT = json.load(open(BASE_DIR / 'static' / 'CrawledData' /
                   'gametimeNew.json'))[team_name].keys()

    dates = set()
    dates.update(SH)
    dates.update(TP)
    dates.update(GT)
    print(dates)
    return dates


def getData(team_name):
    SH = json.load(open(BASE_DIR / 'static' / 'CrawledData' /
                   'stubHubNew.json'))[team_name]
    TP = json.load(open(BASE_DIR / 'static' / 'CrawledData' /
                   'tickpickNew.json'))[team_name]
    GT = json.load(open(BASE_DIR / 'static' / 'CrawledData' /
                   'gametimeNew.json'))[team_name]

    return SH, TP, GT
