"""
Implementation of an inverted index data structure.

An inverted index is a mapping of words to their locations in a document or corpus.
It's used for efficient search and retrieval of documents based on keywords.

This module provides the basic implementation of an inverted index, including:

*   `InvertedIndex`: A class representing the inverted index itself.
    It stores the mapping of words to their locations (document IDs).
*   `Document`: A simple dataclass representing a document with its ID and content.
"""

from typing import Dict, Set

class Document:
    """A simple dataclass representing a document with its ID and content."""
    def __init__(self, id: int, content: str):
        self.id = id
        self.content = content


class InvertedIndex:
    """
    A class representing the inverted index itself.
    
    It stores the mapping of words to their locations (document IDs).
    """

    def __init__(self):
        """Initialize an empty inverted index."""
        self.index: Dict[str, Set[int]] = {}

    def add_document(self, document: Document) -> None:
        """
        Add a document to the index.

        Args:
            document (Document): The document to be added.
        """
        words = document.content.split()
        for word in words:
            if word not in self.index:
                self.index[word] = set()
            self.index[word].add(document.id)

    def search(self, query: str) -> Set[int]:
        """
        Search the index for documents containing a given query.

        Args:
            query (str): The query to be searched.

        Returns:
            Set[int]: A set of document IDs matching the query.
        """
        if query in self.index:
            return self.index[query]
        else:
            return set()


# Example usage
if __name__ == "__main__":
    inverted_index = InvertedIndex()

    doc1 = Document(1, "This is a sample document.")
    doc2 = Document(2, "Another document with the same words.")

    inverted_index.add_document(doc1)
    inverted_index.add_document(doc2)

    print(inverted_index.search("sample"))  # Output: {1}
    print(inverted_index.search("document"))  # Output: {1, 2}
