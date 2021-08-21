from selenium import webdriver
from time import sleep
from helperFunctions import getPlatform, getUrl
import json
import calendar

CHROMEDRIVER_LOCATION = getPlatform()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']) # To remove the "Chrome is being controlled by automated test software" notification
# chrome_options.add_argument("--headless") # To make The Browser not appear HeadlessChrome

driver = webdriver.Chrome(executable_path = str(CHROMEDRIVER_LOCATION), options = chrome_options)

temp_lst = []
data = {}

def get_team_info():
    name = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[3]/div/div[5]/a").text 
    event_details = []
    # container = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/*")
    container = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]")
    teams = container.find_elements_by_tag_name('div')
    for team in teams:
        if team.get_attribute('class') == "_3M6itQDhXMCuHDczUt2vHq _2c2KjM_rU1fn7ZCal1wUIO":
            # location = team.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[2]/div[3]/div/span[5]").text
            day = team.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[1]/div[2]").text
            month = team.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[1]/div[1]").text
            price = team.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[2]/div[1]").text
            title = team.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[2]/div[2]").text
            

            eventData = {
                'Date': {
                    'Day': day.upper(),
                    # 'Month': calendar.month_name(month.split('/')[0]),
                    'Month': month.split('/')[0],
                    'date': month.split('/')[1]
                },
                'title': title,
                'location': [],
                'price': price

                }
            event_details.append(eventData)
            
    data[name] = event_details

for url in getUrl(2):
    driver.get(url)
    get_team_info()

json_object = json.dumps(data)
  
# Writing to sample.json
with open("gametime.json", "w") as outfile:
    outfile.write(json_object)

    """ for team in container:
    if team.get_attribute('class') == "_3M6itQDhXMCuHDczUt2vHq _2c2KjM_rU1fn7ZCal1wUIO":
            day = team.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[1]/div[2]").text
            month = team.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[1]/div[1]").text
            price = team.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[2]/div[1]").text
            title = team.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[2]/div[2]").text
            location = team.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[2]/div[3]/div/span[5]").text

            eventData = {
                    'Date': {
                        'Day': day.upper(),
                        'Month': calendar.month_name(month.split('/')[0]),
                        'date': month.split('/')[1]
                    },
                    'location': location.split('-')[1],
                    'title': title,
                    'price': price

                }
            event_details.append(eventData)
    data[name.strip(' ')[0:2]] = event_details """




