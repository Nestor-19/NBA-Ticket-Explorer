from selenium import webdriver
from time import sleep
from helperFunctions import getPlatform, getUrl
import json

CHROMEDRIVER_LOCATION = getPlatform()
URLS = getUrl(1)
EVENTS_CONTAINER_XPATH = "/html/body/div[1]/div/div/main/div/div/div[2]/div[1]/section/div[2]"

def getDateDetails(fullDate):
    dateDetails = fullDate.split(" ")
    return dateDetails[0], dateDetails[1][:-1]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']) # To remove the "Chrome is being controlled by automated test software" notification
# chrome_options.add_argument("--headless") # To make The Browser not appear HeadlessChrome

driver = webdriver.Chrome(executable_path = str(CHROMEDRIVER_LOCATION), options = chrome_options)

data = {}
for url in URLS:
    driver.get(url)

    teamName = driver.find_element_by_class_name("Breadcrumbs__name").text
    events = driver.find_element_by_xpath(EVENTS_CONTAINER_XPATH).find_elements_by_class_name("EventItem")

    print(teamName)
    eventsDetails = []
    for event in events:
        day = event.find_element_by_class_name("DateStamp__Day").text
        fullDate = event.find_element_by_class_name("DateStamp__MonthDateYear").text
        month, date = getDateDetails(fullDate)
        title = event.find_element_by_class_name("EventItem__TitleLink").text
        location = event.find_element_by_class_name("EventItem__MixInfo").text.replace("\n", " ")
        try:
            price = event.find_element_by_class_name("EventItem__Price").text
        except:
            price = None

        eventData = {
            "Date" : {
                "Day" : day,
                "Month" : month,
                "date" : date
            },
            "title" : title,
            "location" : location,
            "price" : price
        }
        eventsDetails.append(eventData)

    data[teamName] = eventsDetails

json_object = json.dumps(data)
  
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)