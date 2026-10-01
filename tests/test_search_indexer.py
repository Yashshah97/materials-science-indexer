"""Smoke tests for search_indexer."""
import unittest

from materials_science_indexer import search_indexer


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(search_indexer, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(search_indexer) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
