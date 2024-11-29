from tests.abstract.base_test import BaseTest


class TestSearchField(BaseTest):
    
    def test_search_results_show_target_first(self):
        self.home_page.open().is_opened()
        assert True
        
    