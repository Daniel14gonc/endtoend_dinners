from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()
driver.get("http://localhost:19006/")

web_element = driver.find_element(By.ID, 'usuario')
web_element.send_keys('Aristondo01')

time.sleep(2)
print("hola")
web_element = driver.find_element(By.ID, 'password')
web_element.send_keys('Prueba')

time.sleep(2)

web_element = driver.find_element(By.ID, 'loginButton')
web_element.send_keys(Keys.ENTER)

