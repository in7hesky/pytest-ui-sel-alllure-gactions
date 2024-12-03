from tests.abstract.base_test import BaseTest
from pytest_check import check

SEARCH_TARGET = "Falcon 9"

class TestOrderRegistration(BaseTest):
    
    def test_register_order_with_min_required_data(self, valid_user_data):
        
        self.home_page.open()
        self.home_page.search_field_input(SEARCH_TARGET)
        
        check.is_in(SEARCH_TARGET, 
                    self.search_results_page.get_page_title_string())
        check.is_in(SEARCH_TARGET, 
                    self.search_results_page.get_product_by_index(0).text)
        
        self.search_results_page.add_product_by_index(0)
        
        check.is_true(self.search_results_page.check_minicart_count_equals(1))
        
        self.search_results_page.navigation.to_cart()
        
        check.is_true(self.cart_page.check_total_cart_items_equals(1))
        check.equal(self.cart_page.get_cart_item_quantity_by_index(0), 1)
        
        self.cart_page.click_checkout_button()
        
        check.is_true(self.checkout_page.check_cart_item_quantity_equals(1))
        check.is_true(self.checkout_page
                      .check_cart_item_by_name_exists(SEARCH_TARGET))
        
        self.checkout_page.input_required_userdata(valid_user_data)
        self.checkout_page.click_submit_button()
        
        check.is_true(self.order_received_page
            .check_success_notification_is_present())
        