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

driver.get('https://www.nba.com/teams')
sleep(2)
imgTags = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[3]/section/div/div[2]').find_elements_by_tag_name('img')
names = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/section/div/div[2]').find_elements_by_class_name(
    'TeamFigure_tfMainLink__mH93D')
print(len(names), len(imgTags))
lst = {}
i = 0
for tg in imgTags:
    lst[names[i].text] = tg.get_attribute('src')
    i += 1

json_object = json.dumps(lst)

# Writing to sample.json
with open("logos.json", "w") as outfile:
    outfile.write(json_object)
