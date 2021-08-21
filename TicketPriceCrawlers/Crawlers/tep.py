import json
import calendar 
f = open('D:/Python Projects And Codes/Django Projects/SlamDunkHacks/gametime.json')
    
# returns JSON object as 
# a dictionary
data = json.load(f)

for k in data:
    for idx,event in enumerate(data[k]):
        data[k][idx]['Date']['Month'] = calendar.month_abbr[int(event['Date']['Month'])].upper()

json_object = json.dumps(data)
  
# Writing to sample.json
with open("gametime2.json", "w") as outfile:
    outfile.write(json_object)