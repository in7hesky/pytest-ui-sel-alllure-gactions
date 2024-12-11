import allure
import pytest
from tests.abstract.base_test import BaseTest


@allure.feature("Order registration")
class TestOrderRegistration(BaseTest):
    @allure.title("Test registering order with min required valid data E2E")
    @allure.severity("Critical")
    @pytest.mark.parametrize("search_target", ["Falcon 9", "Saturn V"])
    def test_register_order_with_min_required_data(
        self, search_target, valid_user_data):

        self.home_page.open().search_field_input(search_target)

        assert search_target in \
            self.search_results_page.get_product_by_index(0).text

        self.search_results_page.add_product_to_cart_by_index(0)

        assert self.search_results_page.check_minicart_count_equals(1)

        self.search_results_page.navigation.to_cart()

        assert self.cart_page.check_total_cart_items_equals(1)
        assert self.cart_page.get_cart_item_quantity_by_index(0) == 1

        self.cart_page.click_checkout_button()

        assert self.checkout_page.check_cart_item_quantity_equals(1)
        assert self.checkout_page \
            .check_cart_item_by_name_exists(search_target)

        self.checkout_page.input_required_userdata(valid_user_data) \
            .click_submit_button()

        assert self.order_received_page.check_success_notification_is_present()
