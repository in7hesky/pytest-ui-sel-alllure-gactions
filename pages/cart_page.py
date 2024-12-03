from pages.abstract.openable_page import OpenablePage
from config.paths import Paths

class CartPage(OpenablePage):
    
    PAGE_URL = Paths.CART
    
    CART_ITEM_SELECTOR = ("class name", "cart_item")
    QUANTITY_SELECTOR = ("class name", "input-text")
    CHECKOUT_BUTTON_SELECTOR = ("class name", "checkout-button")
    
    def check_total_cart_items_equals(self, target: int):
        return target == len(self.find_elements(self.CART_ITEM_SELECTOR))
    
    def get_cart_item_quantity_by_index(self, index: int):
        quantity_value = self.find_elements(self.CART_ITEM_SELECTOR)[index] \
            .find_element(*self.QUANTITY_SELECTOR).get_attribute("value")
            
        return int(quantity_value or 0)
    
    def click_checkout_button(self):
        self.find_element(self.CHECKOUT_BUTTON_SELECTOR).click()