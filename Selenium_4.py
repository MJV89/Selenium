
#CAMBIAR VENTANAS O PESTAÑAS

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\marki\Desktop\Selenium\chromedriver.exe")

    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get("http://www.google.com")# abrir Google
        time.sleep(3)

        driver.execute_script("window.open('');")# abrir una pestaña
        time.sleep(3)

        driver.switch_to.window(driver.window_handles[1])# posicionate en la pestaña 1
        driver.get("http://www.stackoverflow.com")# carga link en la otra pestaña
        time.sleep(3)

        driver.switch_to.window(driver.window_handles[0])# vuelve a la pestaña principal
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()