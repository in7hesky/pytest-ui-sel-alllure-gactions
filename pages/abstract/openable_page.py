from selenium.webdriver.support import expected_conditions as EC
import allure
from pages.abstract.base_page import BasePage


class OpenablePage(BasePage):

    def open(self):
        with allure.step(f"Open page with url={self.PAGE_URL}"):
            self.driver.get(self.PAGE_URL)
            return self

    def is_opened(self):
        with allure.step(f"Check page is opened with url={self.PAGE_URL}"):
            self.wait.until(EC.url_to_be(f"{self.PAGE_URL}/"))
            return self
