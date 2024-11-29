from config.paths import Paths
from pages.abstract.openable_page import OpenablePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.search_results_page import SearchResultsPage


class HomePage(OpenablePage):
    
    PAGE_URL = Paths.HOME
    
    def search_field_input(self, input: str):
        search_field = self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD_SELECTOR))
        search_field.send_keys(input)
        search_field.send_keys(Keys.ENTER)
        return SearchResultsPage()
        