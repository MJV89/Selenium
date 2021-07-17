
#IR A LA PAGINA ANTERIOR O SIGUIENTE

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\marki\Desktop\Selenium\chromedriver.exe")

    def test_pagina_siguiente_o_anterior(self):
        driver = self.driver
        driver.get("http://www.gmail.com")
        time.sleep(3)

        driver.get("http://www.google.com")
        time.sleep(3)

        driver.get("http://www.youtube.com")
        time.sleep(3)

        driver.back() #vuelve a la pagina anterior
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward() # va a la pagina siguiente
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()