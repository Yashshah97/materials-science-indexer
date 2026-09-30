import unittest
from materials_science_indexer import ranker

class TestRanker(unittest.TestCase):
    def test_rank_search_results(self):
        query_terms = {'term1': 0.5, 'term2': 0.3}
        document_terms = {
            'doc1': {'term1': 10, 'term2': 20},
            'doc2': {'term1': 15, 'term2': 30},
            'doc3': {'term1': 20, 'term2': 40}
        }
        scores = ranker.rank_search_results(query_terms, document_terms)
        self.assertEqual(len(scores), len(document_terms))
        for doc_id in scores:
            self.assertGreaterEqual(scores[doc_id], 0)

    def test_rank_search_results_empty_query(self):
        query_terms = {}
        document_terms = {
            'doc1': {'term1': 10, 'term2': 20},
            'doc2': {'term1': 15, 'term2': 30},
            'doc3': {'term1': 20, 'term2': 40}
        }
        scores = ranker.rank_search_results(query_terms, document_terms)
        self.assertEqual(len(scores), len(document_terms))
        for doc_id in scores:
            self.assertGreaterEqual(scores[doc_id], 0)

    def test_rank_search_results_empty_document(self):
        query_terms = {'term1': 0.5, 'term2': 0.3}
        document_terms = {}
        scores = ranker.rank_search_results(query_terms, document_terms)
        self.assertEqual(len(scores), 0)

if __name__ == "__main__":
    unittest.main()
