
#Xpath
#Es una estructura de objetos (arbol,ruta,etc.. de carpetas por ejemplo)

#Xpath relativo busca en toda la ruta el objeto por mas que cambie de lugar y se mantenga en el un lugar de la ruta
# EJ: //*[@id="input"] barra de busquedad Google
#EJ 2: /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input

#Xpath absoluto busca en un lugar concreto, si se mueve el objeto no lo encontrara
#EJ: /html/body/ntp-app//div[1]/ntp-realbox//div/input barra de busqueda Google

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\marki\Desktop\Selenium\chromedriver.exe")

    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        buscar_xpath = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        time.sleep(3)
        buscar_xpath.send_keys("selenium", Keys.ARROW_DOWN)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()




