import json

# Opening JSON file
f = open('stubHub.json')

# returns JSON object as
# a dictionary
data = json.load(f)

for team in data:
    newDict = {}
    for event in data[team]:
        dateObj = event["Date"]
        dateStrKey = f'{dateObj["date"]} {dateObj["Month"]}, {dateObj["Day"]}'

        tempEvent = event
        del tempEvent["Date"]
        newDict[dateStrKey] = tempEvent
    data[team] = newDict

json_object = json.dumps(data)

# Writing to sample.json
with open("stubHubNew.json", "w") as outfile:
    outfile.write(json_object)
