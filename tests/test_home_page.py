import time
import unittest

from selenium import webdriver as wd
from selenium.webdriver.common.by import By

from pages.home_page import HomePage


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = wd.Chrome(executable_path=r"./wd/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get('http://www.automationpractice.com')

    def test_can_search_for_products(self):
        hp = HomePage(self.driver)
        time.sleep(5)
        sp = hp.perform_search("Dress")
        search_count = sp.get_search_items_list_count()
        self.assertEqual(search_count, 7)

    def test_can_navigate_to_contact_us(self):
        hp = HomePage(self.driver)
        time.sleep(5)
        sp = hp.perform_search("Dress")
        search_count = sp.get_search_items_list_count()
        self.assertEqual(search_count, 7)

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
