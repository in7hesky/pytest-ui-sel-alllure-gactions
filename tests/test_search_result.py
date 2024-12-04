import allure
from tests.abstract.base_test import BaseTest
import pytest


SEARCH_TARGET = "Falcon 9"

@allure.feature("Search Query Results")
class TestSearchResult(BaseTest):
       
    @pytest.fixture(autouse=True)
    def search_query(self, setup):
        self.home_page.open().search_field_input(SEARCH_TARGET)

    @allure.title("Test first search result item has target name")
    @allure.severity("Critical")
    def test_first_result_item_has_target_name(self):
        assert SEARCH_TARGET in \
            self.search_results_page.get_product_by_index(0).text

    @allure.title("Test search results page title equals query prompt")
    @allure.severity("Critical")
    def test_result_page_title_equals_query_prompt(self):
        assert SEARCH_TARGET in self.search_results_page.get_page_title_string()
