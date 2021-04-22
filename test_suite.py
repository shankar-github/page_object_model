import unittest

import os

from HTMLTestRunner import HTMLTestRunner

from tests.test_contact_us_page import ContactUsTest
from tests.test_home_page import  HomePageTest


current_directory = os.getcwd()


class TestSuite(unittest.TestCase):

    def test_execute_suite(self):
        # Create a TestSuite comprising the two test cases
        consolidated_test = unittest.TestSuite()

        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(HomePageTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContactUsTest)
        ])

        output_file = open(current_directory + "/reports/HTML_Test_Runner_ReportTest.html", "w")

        html_runner = HTMLTestRunner.HTMLTestRunner(
            stream=output_file,
            title='HTML Reporting using PyUnit',
            description='HTML Reporting using PyUnit & HTMLTestRunner'
        )

        html_runner.run(consolidated_test)


if __name__ == '__main__':
    unittest.main()
