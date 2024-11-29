from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    
    SEARCH_FIELD_SELECTOR = ("id", "woocommerce-product-search-field-0")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 14, 1)
    