import allure


class GlobalNavSection():
    
    def __init__(self, driver):
        self.driver = driver
    
    def to_cart(self):
        self.__go_by_href_keyword("cart")
    
    def __go_by_href_keyword(self, keyword):
        with allure.step(f"Go to {keyword} page via nav-menu"):
            self.driver.find_element(
                *("xpath", 
                f"//ul[@class='nav-menu']//a[contains(@href, '{keyword}')]")) \
                    .click()
