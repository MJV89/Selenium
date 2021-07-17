# Explicit Wait

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By # buscas un elemento en concreto
from selenium.webdriver.support.ui import WebDriverWait # cargas de paginas hasta encontrar el elemento, para evitar los time.sleep
from selenium.webdriver.support import expected_conditions as EC # poner una condicion de busqueda

class usando_unittest (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\marki\Desktop\Selenium\chromedriver.exe")

    def test_usando_Ecplicit_wait(self):
        driver = self.driver
        driver.get("http://www.google.com")

# Llamamos al explicit wait, le decimos que cargue 10 veces la pagina hasta encontrar el elemento "q" ne este caso
        try:
            element = WebDriverWait(driver, 10) .until (EC.presence_of_element_located ((By.NAME, 'q')))
        finally:
            driver.quit()

if __name__ == '__main__':
    unittest.main()