import unittest
from materials_science_indexer import inverted_index

class TestInvertedIndex(unittest.TestCase):
    def test_add_document(self):
        index = inverted_index.InvertedIndex()
        doc1 = inverted_index.Document(1, "This is a sample document.")
        index.add_document(doc1)
        self.assertIn("sample", index.index)
        self.assertEqual(index.index["sample"], {1})

    def test_search(self):
        index = inverted_index.InvertedIndex()
        doc1 = inverted_index.Document(1, "This is a sample document.")
        index.add_document(doc1)
        self.assertEqual(index.search("sample"), {1})
        self.assertEqual(index.search("document"), set())

if __name__ == "__main__":
    unittest.main()
