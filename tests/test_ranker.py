"""Smoke tests for ranker."""
import unittest

from materials_science_indexer import ranker


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(ranker, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(ranker) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
