import pytest

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_received_page import OrderReceivedPage

class BaseTest:
    home_page: HomePage
    search_results_page: SearchResultsPage
    cart_page: CartPage
    checkout_page: CheckoutPage
    order_received_page: OrderReceivedPage
    
    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        
        request.cls.home_page = HomePage(driver)
        request.cls.search_results_page = SearchResultsPage(driver)
        request.cls.cart_page = CartPage(driver)
        request.cls.checkout_page = CheckoutPage(driver)
        request.cls.order_received_page = OrderReceivedPage(driver)