import time

from pages.home_page import HomePage
from tests.base_test import BaseTest


class ContactUsTest(BaseTest):

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
