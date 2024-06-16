from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
url_web = ['tiket.com','tokopedia.com','orangsiber.com','demoqa.com','automatetheboringstuff.com']

for i in url_web:
    driver.get('https://'+i+'/')
    driver.minimize_window()
    web_title = driver.title
    print(f"{i} - {web_title}")
    
driver.close()