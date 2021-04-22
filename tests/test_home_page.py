import time

from pages.home_page import HomePage
from tests.base_test import BaseTest


class HomePageTest(BaseTest):

    def test_can_search_for_products(self):
        hp = HomePage(self.driver)
        time.sleep(5)
        sp = hp.perform_search("Dress")
        search_count = sp.get_search_items_list_count()
        self.assertEqual(search_count, 7)

    def test_can_navigate_to_contact_us(self):
        hp = HomePage(self.driver)
        time.sleep(5)
        cp = hp.navigate_to_contact_us()
        time.sleep(5)
        self.assertEqual(cp.get_page_title(), "Contact us - My Store")

    def test_can_navigate_to_sign_in_page(self):
        hp = HomePage(self.driver)
        time.sleep(5)
        cp = hp.navigate_to_sign_in_page()
        time.sleep(5)
        self.assertEqual(cp.get_page_title(), "Login - My Store")
