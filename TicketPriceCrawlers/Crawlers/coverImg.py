from selenium import webdriver
from helperFunctions import getPlatform, getUrl
import json
from time import sleep

CHROMEDRIVER_LOCATION = getPlatform()

chrome_options = webdriver.ChromeOptions()
# To remove the "Chrome is being controlled by automated test software" notification
chrome_options.add_experimental_option(
    "excludeSwitches", ['enable-automation'])
# chrome_options.add_argument("--headless") # To make The Browser not appear HeadlessChrome

driver = webdriver.Chrome(executable_path=str(
    CHROMEDRIVER_LOCATION), options=chrome_options)

temp_lst = []
data = {}


def get_team_info():
    name = ' '.join(driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[4]/main/div[2]/div[2]/div/h1").text.split()[:-1])
    image = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div[4]/main/div[2]/div[1]/img').get_attribute('src')

    data[name] = image


for url in getUrl(2):
    driver.get(url)
    sleep(2)
    get_team_info()

json_object = json.dumps(data)

# Writing to sample.json
with open("cover.json", "w") as outfile:
    outfile.write(json_object)
