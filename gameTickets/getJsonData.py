import json
from SlamDunkHacks.settings import BASE_DIR


def getCoverPage(team_name):
    json_data = open(BASE_DIR / 'static' / 'CrawledData' / 'cover.json')
    data = json.load(json_data)

    return data[team_name]
