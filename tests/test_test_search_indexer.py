import unittest
from materials_science_indexer import test_search_indexer

class TestTestSearchIndexer(unittest.TestCase):

    def test_module_exists(self):
        self.assertTrue(hasattr(test_search_indexer, 'SearchIndexer'))

    def test_SearchIndexer_class_exists(self):
        self.assertTrue(isinstance(test_search_indexer.SearchIndexer(), type))

if __name__ == "__main__":
    unittest.main()
