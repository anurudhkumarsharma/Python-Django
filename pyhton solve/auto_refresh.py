
from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get('https://www.instagram.com/direct/inbox/')
while True:
    time.sleep(20)
    driver.refresh()
driver.quit()