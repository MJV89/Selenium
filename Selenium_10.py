# Select (lista de opciones)

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


class usando_unittest (unittest.TestCase):
    def setUp(self):
        self.diver = webdriver.Chrome(executable_path=r"C:\Users\marki\Desktop\Selenium\chromedriver.exe")

    def test_usando_select(self):
        driver = self.diver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(3)

        select = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")#Buscas el xpath
        opcion = select.find_elements_by_tag_name("option")#el elemeto "option" guarda la lista en la variable "opcion"
        time.sleep(3)

        for opcion in opcion:
            print("Los valores son: %s" % opcion.get_attribute("value"))#Recorre la lista y devuelve los valores(% concatenamos cadenas)
            opcion.click()
            time.sleep(1)

        #Seleccionar una posicion en especifico de la lista
        seleccionar = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("10")
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
