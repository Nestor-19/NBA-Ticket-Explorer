from selenium import webdriver
from time import sleep
from helperFunctions import getPlatform, getUrl
import json


CHROMEDRIVER_LOCATION = getPlatform()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']) # To remove the "Chrome is being controlled by automated test software" notification
# chrome_options.add_argument("--headless") # To make The Browser not appear HeadlessChrome

driver = webdriver.Chrome(executable_path = str(CHROMEDRIVER_LOCATION), options = chrome_options)

data = {}

def get_team_data():
    name = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/span").text
    container = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[1]/*")
    event_details = []
    for event in container:
        event.get_attribute('class')
        if event.get_attribute('class') == "srItem  active allE SPORTSE  ":
            month = event.find_element_by_class_name("dateDisplay").text
            if month == 'TBD':
                continue
            day = event.find_element_by_xpath("./div[1]/span[2]").text
            title = event.find_element_by_tag_name("h3").text
            location = event.find_element_by_class_name("locDisplay").text
            price = event.find_element_by_class_name("minPrice").text


            eventData = {
                'Date': {
                    'Day': day.split(' ')[0].upper(),
                    'Month': month.split(' ')[0].upper(),
                    'date': month.split(' ')[1]
                },
                'location': location.split('-')[1],
                'title': title,
                'price': price.split(' ')[1]

            }
            event_details.append(eventData)
    data[name] = event_details

for url in getUrl(0):
    driver.get(url)
    get_team_data()

json_object = json.dumps(data)
  
# Writing to sample.json
with open("tickpick.json", "w") as outfile:
    outfile.write(json_object)