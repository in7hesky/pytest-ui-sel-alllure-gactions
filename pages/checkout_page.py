from pages.abstract.openable_page import OpenablePage
from config.paths import Paths
from selenium.webdriver.support.ui import Select


class CheckoutPage(OpenablePage):
    
    PAGE_URL = Paths.CHECKOUT
    
    CART_ITEM_SELECTOR = ("class name", "cart_item")
    
    FIRSTNAME_SELECTOR = ("id", "billing_first_name")
    LASTNAME_SELECTOR = ("id", "billing_last_name")
    COUNTRY_SELECTOR = ("id", "billing_country")
    STREET_SELECTOR = ("id", "billing_address_1")
    CITY_SELECTOR = ("id", "billing_city")
    STATE_SELECTOR = ("id", "billing_state")
    ZIP_SELECTOR = ("id", "billing_postcode")
    PHONE_SELECTOR = ("id", "billing_phone")
    EMAIL_SELECTOR = ("id", "billing_email")
    
    SUBMIT_BUTTON_SELECTOR = ("id", "place_order")
    
    def check_cart_item_by_name_exists(self, name: str):
        for element in self.find_elements(self.CART_ITEM_SELECTOR):
            if name in element.text:
                return True
        return False
    
    def check_cart_item_quantity_equals(self, target: int):
        return target == len(self.find_elements(self.CART_ITEM_SELECTOR))
    
    def input_required_userdata(self, userdata: dict[str, str]):
        self.input_firstname(userdata["firstname"])
        self.input_lastname(userdata["lastname"])
        self.input_country(userdata["country"])
        self.input_street(userdata["street"])
        self.input_city(userdata["city"])
        self.input_state(userdata["state"])
        self.input_ZIP(userdata["ZIP"])
        self.input_phone(userdata["phone"])
        self.input_email(userdata["email"])
    
        return self
    
    def input_firstname(self, input: str):
        self.find_element(self.FIRSTNAME_SELECTOR).send_keys(input)
        return self
        
    def input_lastname(self, input: str):
        self.find_element(self.LASTNAME_SELECTOR).send_keys(input)
        return self
        
    def input_country(self, input: str):
        Select(self.find_element(self.COUNTRY_SELECTOR)) \
            .select_by_visible_text(input)
        return self
    
    def input_street(self, input: str):
        self.find_element(self.STREET_SELECTOR).send_keys(input)
        return self
    
    def input_city(self, input: str):
        self.find_element(self.CITY_SELECTOR).send_keys(input)
        return self
        
    def input_state(self, input: str):
        state_input_element = self.find_element(self.STATE_SELECTOR)
        
        if state_input_element.get_attribute("type") == "input":
            state_input_element.send_keys("input")
            return self
        
        Select(state_input_element).select_by_visible_text(input)
        return self
        
    def input_ZIP(self, input: str):
        self.find_element(self.ZIP_SELECTOR).send_keys(input)
        return self
        
    def input_phone(self, input: str):
        self.find_element(self.PHONE_SELECTOR).send_keys(input)
        return self
        
    def input_email(self, input: str):
        self.find_element(self.EMAIL_SELECTOR).send_keys(input)
        return self
    
    def click_submit_button(self):
        self.find_element(self.SUBMIT_BUTTON_SELECTOR).click()
        return self
    
