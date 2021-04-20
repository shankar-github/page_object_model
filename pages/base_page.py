import os
import time
from traceback import print_stack

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def get_element_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + locator_type +
                  " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_element_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            print("Element found with locator: " + str(locator) +
                  " and  locatorType: " + locator_type)
        except:
            print("Element not found with locator: " + str(locator) +
                  " and  locator_type: " + locator_type)
        return element

    def get_element_list(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_element_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            print("Element list found with locator: " + str(locator) +
                  " and  locator_type: " + locator_type)
        except:
            print("Element list not found with locator: " + str(locator) +
                  " and  locator_type: " + locator_type)
        return element

    def element_click(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            print("Clicked on element with locator: " + str(locator) +
                  " locatorType: " + locator_type)
        except:
            print("Cannot click on the element with locator: " + str(locator) +
                  " locatorType: " + locator_type)
            print_stack()

    def type_keys(self, data, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            print("Sent data on element with locator: " + str(locator) +
                  " locator type: " + locator_type)
        except:
            print("Cannot send data on the element with locator: " + str(locator) +
                  " locator type: " + locator_type)
            print_stack()

    def select_from_drop_down(self, select_value, locator, locator_type="id", select_by='index'):
        select_by = select_by.lower()
        try:
            element = self.get_element(locator, locator_type)
            sel = Select(element)
            if select_by == 'val':
                sel.select_by_value(select_value)
            elif select_by == 'index':
                sel.select_by_index(int(select_value))
            elif select_by == 'text':
                sel.select_by_visible_text(select_value)
            else:
                print("Cannot Select with given Select By " + str(select_by) + " And Value " + str(select_value))
        except:
            print("Cannot Select with given Select By " + str(select_by) + " And Value " + str(select_value))
            print_stack()

    def upload_file(self, file_name, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(os.path.abspath(file_name))
        except:
            print("Cannot Upload File With Given Locator " + str(locator) + "And Locator Type " + locator_type)
            print_stack()

    def is_element_present(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def element_presence_check(self, locator, by_type):
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def wait_for_element(self, locator, locator_type="id",
                         time_out=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_element_by_type(locator_type)
            print("Waiting for maximum :: " + str(time_out) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, time_out, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator,
                                                             "stopFilter_stops-0")))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element

    def get_element_text(self, locator="", locator_type="id", element=None, info=""):

        try:
            if locator:  # This means if locator is not empty
                print("In locator condition")
                element = self.get_element(locator, locator_type)
            print("Before finding text")
            text = element.text
            print("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                print("Getting text on element :: " + info)
                print("The text is :: '" + text + "'")
                text = text.strip()
        except:
            print("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def take_screenshot(self, test_case_name):
        file_name = test_case_name + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_filename = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_filename)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            print("Screenshot save to directory: " + destination_file)
        except:
            print("### Exception Occurred when taking screenshot")
            print_stack()
