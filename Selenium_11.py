#click en boton radio (check point)

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\marki\Desktop\Selenium\chromedriver.exe")

    def test_usando_radio_botton(self): #Recordar poner "test" siempre al principio de variable
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
        time.sleep(5)

        radio_bot = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[4]")
        radio_bot.click()
        time.sleep(3)

        radio_bot = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[3]")
        radio_bot.click()
        time.sleep(3)
    
    def tearDown(self): #Cierra el navegador
        self.driver.close()


if __name__ == '__main__': #Para que ejecute el unittest
    unittest.main()


