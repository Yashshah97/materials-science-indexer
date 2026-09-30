import unittest
from materials_science_indexer import search_indexer

class TestSearchIndexer(unittest.TestCase):
    def test_add_document(self):
        index = search_indexer.SearchIndexer()
        index.add_document("doc1", {"lattice_constant": 3.0, "alloy_composition": "Cu50Zn50"})
        self.assertEqual(index.doc_ids, ["doc1"])
        self.assertEqual(index.inverted_index["lattice_constant"], ["doc1"])
        self.assertEqual(index.inverted_index["alloy_composition"], ["doc1"])

    def test_search(self):
        index = search_indexer.SearchIndexer()
        index.add_document("doc1", {"lattice_constant": 3.0, "alloy_composition": "Cu50Zn50"})
        index.add_document("doc2", {"lattice_constant": 3.5, "alloy_composition": "Cu75Zn25"})
        self.assertEqual(index.search(["lattice_constant"]), ["doc1", "doc2"])
        self.assertEqual(index.search(["alloy_composition"]), ["doc1", "doc2"])

    def test_get_document(self):
        index = search_indexer.SearchIndexer()
        index.add_document("doc1", {"lattice_constant": 3.0, "alloy_composition": "Cu50Zn50"})
        self.assertEqual(index.get_document("doc1"), {"lattice_constant": [3.0], "alloy_composition": ["Cu50Zn50"]})

if __name__ == '__main__':
    unittest.main()
