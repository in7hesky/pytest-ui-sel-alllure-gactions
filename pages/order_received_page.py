from pages.abstract.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class OrderReceivedPage(BasePage):
    
    SUCCESS_NOTIFICATION_SELECTOR = (
        "class name", "woocommerce-notice--success")
    
    @allure.step("Check success notification is present")
    def check_success_notification_is_present(self):
        try:
            WebDriverWait(self.driver, 20, 1) \
                .until(EC.visibility_of_element_located(
                    self.SUCCESS_NOTIFICATION_SELECTOR))
        except TimeoutException:
            return False
        else:
            return True
