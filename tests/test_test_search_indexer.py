"""Smoke tests for test_search_indexer."""
import unittest

from materials_science_indexer import test_search_indexer


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(test_search_indexer, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(test_search_indexer) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
