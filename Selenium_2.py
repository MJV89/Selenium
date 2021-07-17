#UNITTEST

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\marki\Desktop\Selenium\chromedriver.exe")

#despues de definir el "setUP" al nombrar variables tiene que tener "test" para ser encontrardas
    def test_buscar(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title) #buscar la palabra "google" en el titulo .title
        elemento = driver.find_element_by_name("q")#barra de busqueda de google se llama "q"
        elemento.send_keys("selenium")
        elemento.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No se encontro el elemento." not in driver.page_source #me dice que no encontro el elemento

    def tearDown(self):
        self.driver.close() #apague al terminar el test

#Cerrar la clase
if __name__ == '__main__':
    unittest.main()
        