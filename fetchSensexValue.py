import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Duration to wait before page refresh
WAIT_TIME = 10;

# Money control URL
url = r"http://www.moneycontrol.com/sensex/bse/sensex-live"

# Path of chromedriver
chromeDriverPath = r"C:\Users\m0pxnn\Documents\Selenium\ChromeDriver\chromedriver.exe" 

# XPATH for sensex value
xPath_sensexValue = "//*[@id=\"mc_mainWrapper\"]/div[3]/div[1]/div[4]/div[1]/strong"

os.environ["webdriver.chrome.driver"] = chromeDriverPath
browser = webdriver.Chrome(executable_path=chromeDriverPath)
browser.set_window_position(-2000, 0)
browser.get(url)

print ("\n\n****** Sensex: ");
while (1):
    sensexValue = browser.find_element(By.XPATH, xPath_sensexValue)
    sensexValue = sensexValue.text
    
    print ("Timestamp  : ", datetime.datetime.now());
    print ("Value      : ", sensexValue);
    print("\n");
    time.sleep(WAIT_TIME);
    browser.refresh();

