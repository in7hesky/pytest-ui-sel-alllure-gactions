import pytest

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


class BaseTest:
    home_page: HomePage
    search_results_page: SearchResultsPage
    
    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        
        request.cls.home_page = HomePage(driver)
        request.cls.search_results_page = SearchResultsPage(driver)