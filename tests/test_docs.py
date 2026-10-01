"""Smoke tests for docs."""
import unittest

from materials_science_indexer import docs


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(docs, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(docs) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
