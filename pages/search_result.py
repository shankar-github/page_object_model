from pages.base_page import BasePage


class SearchResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ##########################################Start Locators##############################################

    _search_results = "//div/h1/span[@class='lighter']"
    _item_list = "//a[@class='product_img_link']/img"

    ##########################################End Locators################################################

    def get_search_results(self):
        return self.get_element_text(locator=self._search_results, locator_type="xpath")

    def get_search_items_list_count(self):
        return len(self.get_element_list(locator=self._item_list, locator_type="xpath"))