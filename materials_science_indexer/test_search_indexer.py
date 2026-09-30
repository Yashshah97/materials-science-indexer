"""
Unit tests for SearchIndexer class.

This module contains unit tests for the SearchIndexer class. These tests verify that the SearchIndexer correctly indexes and searches materials science data.
"""

import unittest
from collections import defaultdict
from typing import Dict, List

class TestSearchIndexer(unittest.TestCase):

    def test_empty_index(self):
        """Test empty index."""
        index = SearchIndexer()
        self.assertEqual(index.search("non-existent"), [])

    def test_single_entry_search(self):
        """Test single entry search."""
        index = SearchIndexer()
        index.add_entry("gold", {"lattice_constant": 4.07})
        result = index.search("gold")
        self.assertEqual(result, [{"material": "gold", "properties": {"lattice_constant": 4.07}}])

    def test_multiple_entries_search(self):
        """Test multiple entries search."""
        index = SearchIndexer()
        index.add_entry("gold", {"lattice_constant": 4.07})
        index.add_entry("silver", {"lattice_constant": 3.92})
        result = index.search("gold")
        self.assertEqual(result, [{"material": "gold", "properties": {"lattice_constant": 4.07}}])

    def test_ranking(self):
        """Test ranking."""
        index = SearchIndexer()
        index.add_entry("gold", {"lattice_constant": 4.07})
        index.add_entry("silver", {"lattice_constant": 3.92, "density": 10.5})
        result = index.search("gold")
        self.assertEqual(result[0]["material"], "gold")

class SearchIndexer:
    def __init__(self):
        """Initialize empty search index."""
        self.index: Dict[str, List[Dict]] = defaultdict(list)

    def add_entry(self, material: str, properties: Dict) -> None:
        """
        Add a new entry to the search index.

        Args:
            material (str): Material name.
            properties (Dict): Material properties.
        """
        self.index[material].append(properties)

    def search(self, query: str) -> List[Dict]:
        """
        Search for materials matching the given query.

        Args:
            query (str): Query string.

        Returns:
            List[Dict]: List of material properties that match the query.
        """
        return [properties for properties in self.index.get(query, [])]

if __name__ == "__main__":
    unittest.main()
