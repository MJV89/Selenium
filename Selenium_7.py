#Implicit wait
#Implicit es de Selenium y Time.sleep es de Python

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\marki\Desktop\Selenium\chromedriver.exe")

    def test_usando_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) #espere 5 segundos igual que el Time.sleep
        driver.get("http://www.google.com")
        #Busqueda dinamica de un elemento, es algo que cambia de nombre constantemente segun su uso
        myDynamicElement = driver.find_element_by_name("q")

if __name__ == '__main__':
    unittest.main()