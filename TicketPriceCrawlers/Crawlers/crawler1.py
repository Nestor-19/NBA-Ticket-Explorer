from selenium import webdriver
from time import sleep
from helperFunctions import getPlatform

CHROMEDRIVER_LOCATION = getPlatform()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']) # To remove the "Chrome is being controlled by automated test software" notification
# chrome_options.add_argument("--headless") # To make The Browser not appear HeadlessChrome

driver = webdriver.Chrome(executable_path = str(CHROMEDRIVER_LOCATION), options = chrome_options)
driver.get("https://www.instagram.com/")
sleep(8)