from selenium import webdriver #ejecutar selenium 
from selenium.webdriver.common.keys import Keys #solitar datos de teclado
import time # pausas y sleep

#SIEMPRE declarar el driver atraves de una variable
driver = webdriver.Chrome(executable_path = r"C:\Users\marki\Desktop\Selenium\chromedriver.exe")

driver.get("https://gmail.com") #ruta abrir en el navegador

usuario = driver.find_element_by_id("identifierId")#casillero para ingresar ID
usuario.send_keys("mjv.ow.01@gmail.com")#ingreso de ID
usuario.send_keys(Keys.ENTER)#apretar ENTER automaticamente despues de ingresar datos

time.sleep(3)#

clave = driver.find_element_by_name("password") #ingreso de contraseña, aveces usan ID otras no
clave.send_keys("chechina")
clave.send_keys(Keys.ENTER)



#DETENER PROCESO CTRL + ALT + M