from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from pages.sections.global_nav_section import GlobalNavSection
import allure


class BasePage:
    
    SEARCH_FIELD_SELECTOR = ("id", "woocommerce-product-search-field-0")
    MINICART_CONTENTS_COUNT_SELECTOR = ("css selector", ".cart-contents .count")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 14, 1)
        self.navigation = GlobalNavSection(driver)
    
    @allure.step("Check minicart quantity equals target")
    def check_minicart_count_equals(self, target: int):
        try:
            self.wait.until(EC.text_to_be_present_in_element(
                    self.MINICART_CONTENTS_COUNT_SELECTOR, f"{target} "))
        except TimeoutException:
            return False
        else:
            return target == int(self.find_element(
                self.MINICART_CONTENTS_COUNT_SELECTOR).text.split()[0])   
    
    @allure.step("Input search query and submit")
    def search_field_input(self, input: str):
        search_field = self.find_element(self.SEARCH_FIELD_SELECTOR)
        search_field.send_keys(input)
        search_field.send_keys(Keys.ENTER)

    def find_element(self, selector):
        return self.wait.until(EC.element_to_be_clickable(selector))
    
    def find_elements(self, selector):
        return self.wait.until(EC.presence_of_all_elements_located(selector))
