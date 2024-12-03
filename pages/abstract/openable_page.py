from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class OpenablePage(BasePage):
    
    def open(self):
        self.driver.get(self.PAGE_URL)
        return self
        
    def is_opened(self):
        self.wait.until(EC.url_to_be(f"{self.PAGE_URL}/"))
        return self
    