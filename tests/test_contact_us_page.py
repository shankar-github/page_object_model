import time
import unittest

from selenium import webdriver as wd

from pages.home_page import HomePage


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = wd.Chrome(executable_path=r"./wd/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get('http://www.automationpractice.com')

    def test_cannot_send_invalid_message(self):
        hp = HomePage(self.driver)
        time.sleep(5)
        cp = hp.navigate_to_contact_us()
        ncp = cp.send_a_message('', '', '', '', '')
        time.sleep(5)
        self.assertIn("There is 1 error", ncp.get_failure_message())

    def test_can_send_valid_message(self):
        hp = HomePage(self.driver)
        time.sleep(5)
        cp = hp.navigate_to_contact_us()
        ncp = cp.send_a_message('1', 'a@b.com', '1',
                                '/home/shankar/python_projects/page_object_model/data/img/flower.jpeg', 'Test Message')
        time.sleep(5)
        self.assertIn("Your message has been successfully sent to our team.", ncp.get_success_message())

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
