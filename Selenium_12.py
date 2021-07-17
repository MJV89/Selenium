#Hover Action
#Sirve para asegurar que los links no tengo errores (de cualquier tipo)

from selenium import webdriver
from selenium.webdriver import ActionChains #Simula el movimiento del mouse
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\marki\Desktop\Selenium\chromedriver.exe")
driver.get("https://www.google.com")
time.sleep(3)

elem = driver.find_element_by_link_text("Privacidad") #Busca la palabra especifica y escrita exactamente igual

hover = ActionChains(driver).move_to_element(elem) # "mover" el mouse al elemento indicado
hover.perform() # quedarse pocisionado en el elemento
time.sleep(5)

driver.quit()