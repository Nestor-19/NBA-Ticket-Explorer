import sys
import os
from pathlib import Path

def getPlatform():
    baseDir = Path(__file__).resolve().parent.parent / 'chromeDrivers'
    if sys.platform == 'win32':
        return baseDir / "Windows" / "chromedriver.exe"
    elif sys.platform == 'darwin':
        return baseDir / "Mac" / "chromedriver"

CHROMEDRIVER_LOCATION = getPlatform()

print(CHROMEDRIVER_LOCATION)