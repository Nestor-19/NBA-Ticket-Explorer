import sys
from pathlib import Path
import json

def getPlatform():
    baseDir = Path(__file__).resolve().parent.parent / 'chromeDrivers'
    if sys.platform == 'win32':
        return baseDir / "Windows" / "chromedriver.exe"
    elif sys.platform == 'darwin':
        return baseDir / "Mac" / "chromedriver"

def getUrl(urlIndex):
    baseDir = Path(__file__).resolve().parent.parent
  
    # Opening JSON file
    f = open(baseDir / 'crawlerSites.json',)
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)

    return data['sites'][urlIndex]