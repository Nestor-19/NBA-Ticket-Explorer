from selenium import webdriver
from helperFunctions import getPlatform, getUrl
import json
from time import sleep

CHROMEDRIVER_LOCATION = getPlatform()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']) # To remove the "Chrome is being controlled by automated test software" notification
# chrome_options.add_argument("--headless") # To make The Browser not appear HeadlessChrome

driver = webdriver.Chrome(executable_path = str(CHROMEDRIVER_LOCATION), options = chrome_options)

temp_lst = []
data = {}

def get_team_info():
    name = ' '.join(driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[2]/div[2]/div/h1").text.split()[:-1])
    event_details = []
    # container = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/*")
    container = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]")
    teams = container.find_elements_by_tag_name('div')
    print(name,len(teams))
    for team in teams:
        if team.get_attribute('class') == "_3M6itQDhXMCuHDczUt2vHq _2c2KjM_rU1fn7ZCal1wUIO":
            try:
                location = team.find_elements_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[2]/div[3]/div/*")[-1].text
            except:
                location = "None"
            day = team.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[1]/div[2]").text
            month = team.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[1]/div[1]").text
            price = team.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[2]/div[1]").text
            title = team.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/main/div[3]/section[1]/a[1]/div/div/div[2]/div[2]").text
            

            eventData = {
                'Date': {
                    'Day': day.upper(),
                    'Month': month.split('/')[0],
                    'date': month.split('/')[1]
                },
                'title': title,
                'location': location,
                'price': price

                }
            event_details.append(eventData)
            
    data[name] = event_details

for url in getUrl(2):
    driver.get(url)
    sleep(2)
    get_team_info()

json_object = json.dumps(data)
  
# Writing to sample.json
with open("gametime.json", "w") as outfile:
    outfile.write(json_object)