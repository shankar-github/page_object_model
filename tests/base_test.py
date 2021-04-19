import time
import unittest

from selenium import webdriver as WD
from selenium.webdriver.common.by import By

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WD.Chrome(executable_path=r"./wd/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get('http://www.automationpractice.com')

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
