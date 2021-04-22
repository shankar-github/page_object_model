from .base_page import BasePage
from pages.search_result import SearchResultPage

class ContactUsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)


    ##########################################Start Locators##############################################

    _subject_heading = "id_contact"
    _email_address = "email"
    _order_reference = "id_order"
    _attach_file = "uniform-fileUpload"
    _message = "message"
    _send = "submitMessage"
    _failure_message ="//div[@class='alert alert-danger']"
    _success_message = "//p[@class='alert alert-success']"

    ##########################################End Locators################################################

    def _choose_subject_heading(self, select_val):
        self.select_from_drop_down(select_value=select_val,locator=self._subject_heading, locator_type='id',select_by='index')

    def _type_email_address(self, email_address):
        self.type_keys(email_address,self._email_address, locator_type="id")

    def _type_order_reference(self, order_ref):
        self.type_keys(order_ref,self._order_reference, locator_type="id")

    def _attach_file(self, file_path):
        self.upload_file(file_path,self._attach_file, locator_type="id")

    def _type_message(self, message):
        self.type_keys(message,self._message, locator_type="id")

    def _click_send(self):
        self.element_click(self._send, locator_type="id")

    def send_a_message(self,sub_heading, email_address, order_ref,file_path,message):
        if sub_heading and email_address and message:
            self._choose_subject_heading(sub_heading)
            self._type_email_address(email_address)
            self._type_order_reference(order_ref)
            self._attach_file(file_path)
            self._type_message(message)
            self._click_send()
        else:
            self._click_send()
        return ContactUsPage(self.driver)

    def get_success_message(self):
        return self.get_element_text(locator=self._success_message, locator_type="xpath")

    def get_failure_message(self):
        return self.get_element_text(locator=self._failure_message, locator_type="xpath")
