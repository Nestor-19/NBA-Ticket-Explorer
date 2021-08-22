import json
import calendar

# Opening JSON file
f = open('gametime.json')

# returns JSON object as
# a dictionary
data = json.load(f)

for team in data:
    newDict = {}
    for event in data[team]:
        dateObj = event["Date"]
        mm = calendar.month_abbr[int(dateObj["Month"])].upper()
        dateStrKey = f'{dateObj["date"]} {mm}, {dateObj["Day"]}'

        tempEvent = event
        del tempEvent["Date"]
        newDict[dateStrKey] = tempEvent
    data[team] = newDict

json_object = json.dumps(data)

# Writing to sample.json
with open("gametimeNew.json", "w") as outfile:
    outfile.write(json_object)
