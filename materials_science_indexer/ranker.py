def rank_search_results(query_terms, document_terms):
    """
    Calculate a score for each document in the search results based on relevance.

    The score is calculated as the dot product of the query terms and document terms,
    normalized by the length of both vectors. This is a simple implementation of TF-IDF.

    :param query_terms: A dictionary mapping term to weight
    :type query_terms: dict[str, float]
    :param document_terms: A dictionary mapping term to weight
    :type document_terms: dict[str, float]
    :return: A dictionary mapping document ID to score
    :rtype: dict[str, float]
    """
    scores = {}
    for doc_id, terms in document_terms.items():
        dot_product = sum(query_term * terms.get(term, 0) for term, query_term in query_terms.items())
        length_query = sum(abs(x) for x in query_terms.values())
        length_doc = sum(abs(x) for x in terms.values())
        score = dot_product / (length_query * length_doc)
        scores[doc_id] = score
    return scores

def main():
    """
    Test the rank_search_results function.
    """
    query_terms = {'term1': 0.5, 'term2': 0.3}
    document_terms = {
        'doc1': {'term1': 10, 'term2': 20},
        'doc2': {'term1': 15, 'term2': 30},
        'doc3': {'term1': 20, 'term2': 40}
    }
    print(rank_search_results(query_terms, document_terms))

if __name__ == "__main__":
    main()
