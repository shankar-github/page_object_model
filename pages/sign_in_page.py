from .base_page import BasePage
from .search_result import SearchResultPage


class SignInPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)


    ##########################################Start Locators##############################################

    _search_box = "search_query_top"
    _search_button = "submit_search"
    _contact_us_link = "Contact us"
    _sign_in_link = "Sign in"

    ##########################################End Locators################################################

    def _enter_search_text(self, search_text ="SEARCH", ):
        self.type_keys(search_text, self._search_box, locator_type="id")

    def _click_search_button(self):
        self.element_click(self._search_button, locator_type="name")

    def _click_contact_us_link(self):
        self.element_click(self._contact_us_link, locator_type="link")

    def _click_contact_us_link(self):
        self.element_click(self._sign_in_link, locator_type="link")

    def perform_search(self,search_for):
        self._enter_search_text(search_for)
        self._click_search_button()
        return SearchResultPage(self.driver)

    def navigate_to_contact_us(self):
        self._click_contact_us_link()

    def navigate_to_sign_in_page(self):
        self._contact_us_link()
