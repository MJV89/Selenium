# Displayed Element

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\marki\Desktop\Selenium\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(3)

displayElemen = driver.find_element_by_name("btnI")
time.sleep(3)

print(displayElemen.is_displayed()) # regresa True o False si logro cargar el elemento
time.sleep(3)

print(displayElemen.is_enabled())# regresa un True o False si el elemento esta disponible

