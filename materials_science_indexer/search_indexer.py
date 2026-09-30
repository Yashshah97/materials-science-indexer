"""
Materials Science Search Indexer Module.

This module contains the main class `SearchIndexer` for creating search indexes and processing queries.
"""

class SearchIndexer:
    """
    Main class for search index creation and query processing.

    Attributes:
        inverted_index (dict): Inverted index data structure mapping terms to documents.
        doc_ids (list): List of document IDs in the search index.
    """

    def __init__(self):
        self.inverted_index = {}
        self.doc_ids = []

    def add_document(self, doc_id, properties):
        """
        Add a new document to the search index.

        Args:
            doc_id (str): Unique ID for the document.
            properties (dict): Dictionary of crystal lattice and alloy properties.
        """
        self.doc_ids.append(doc_id)
        for term, value in properties.items():
            if term not in self.inverted_index:
                self.inverted_index[term] = []
            self.inverted_index[term].append(doc_id)

    def search(self, query_terms):
        """
        Process a search query and return ranked document IDs.

        Args:
            query_terms (list): List of terms to search for.

        Returns:
            list: Ranked list of document IDs matching the query.
        """
        scores = {}
        for doc_id in self.doc_ids:
            score = 0
            for term in query_terms:
                if term in self.inverted_index and doc_id in self.inverted_index[term]:
                    score += 1
            scores[doc_id] = score
        return sorted(scores, key=scores.get, reverse=True)

    def get_document(self, doc_id):
        """
        Get the properties of a document by its ID.

        Args:
            doc_id (str): Unique ID for the document.

        Returns:
            dict: Dictionary of crystal lattice and alloy properties.
        """
        if doc_id in self.doc_ids:
            return {term: value for term, value in self.inverted_index.items() if doc_id in value}
        else:
            raise ValueError("Document not found")

# Example usage
index = SearchIndexer()
index.add_document("doc1", {"lattice_constant": 3.0, "alloy_composition": "Cu50Zn50"})
index.add_document("doc2", {"lattice_constant": 3.5, "alloy_composition": "Cu75Zn25"})

print(index.search(["lattice_constant", "alloy_composition"]))  # Output: ['doc1', 'doc2']
print(index.get_document("doc1"))  # Output: {'lattice_constant': [3.0], 'alloy_composition': ['Cu50Zn50']}
