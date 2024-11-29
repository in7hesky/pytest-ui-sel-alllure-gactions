from pages.abstract.base_page import BasePage


class SearchResultsPage(BasePage):
    
    PRODUCT_SELECTOR = ("css", ".product")
    
    @property
    def results(self):
        return self.driver.find_elements(self.PRODUCT_SELECTOR)