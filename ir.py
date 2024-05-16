

def query_likelihood_ranking(query, documents, smoothing=0.1):
    ranked_documents = []
    for i, doc in enumerate(documents):
        likelihood = 1.0
        doc_terms = list(doc.keys())
        for term in query:
            term_freq = doc_terms.count(term)
            doc_length = len(doc_terms)
            prob_term = (term_freq + smoothing) / (doc_length + smoothing * len(set(term for doc in documents for term in doc.keys())))
            likelihood *= prob_term
        ranked_documents.append((i, likelihood))
    
    # Sorting the documents by likelihood using selection sort
    for i in range(len(ranked_documents)):
        max_index = i
        for j in range(i+1, len(ranked_documents)):
            if ranked_documents[j][1] > ranked_documents[max_index][1]:
                max_index = j
        ranked_documents[i], ranked_documents[max_index] = ranked_documents[max_index], ranked_documents[i]
    
    result_dict = dict(ranked_documents)
    return result_dict

def jelinek_mercer_ranking(query, documents, lambda_param=0.5):
    ranked_documents = []
    for i, doc in enumerate(documents):
        likelihood = 1.0
        doc_terms = list(doc.keys())
        for term in query:
            term_freq = doc_terms.count(term)
            doc_length = len(doc_terms)
            prob_term = (1 - lambda_param) * (term_freq / doc_length) + lambda_param * collection(term, documents)
            likelihood *= prob_term
        ranked_documents.append((i, likelihood))
    
    # Sorting the documents by likelihood using selection sort
    for i in range(len(ranked_documents)):
        max_index = i
        for j in range(i+1, len(ranked_documents)):
            if ranked_documents[j][1] > ranked_documents[max_index][1]:
                max_index = j
        ranked_documents[i], ranked_documents[max_index] = ranked_documents[max_index], ranked_documents[i]
    
    result_dict = dict(ranked_documents)
    return result_dict

def collection(term, corpus):
    total_terms = sum(len(doc.keys()) for doc in corpus)
    term_freq = sum(term in doc for doc in corpus)
    if total_terms == 0:
        return 0
    else:
        return term_freq / total_terms

def main():
    doc_input = input("Enter the list of documents (each document should be a string in the format 'doc , doc , ....' ): ")
    doc_strings = doc_input.split(', ')
    documents = []
    for doc_str in doc_strings:
        doc_terms = doc_str.split()
        doc_dict = {}
        for i, term in enumerate(doc_terms):
            if term in doc_dict:
                doc_dict[term].append(i)
            else:
                doc_dict[term] = [i]
        documents.append(doc_dict)

    query_input = input("Enter the query (in the format 'term1 term2 ...'): ")
    query = query_input.split()
    query_dict = {term: [] for term in query}
    for term in query:
        for i, doc in enumerate(documents):
            if term in doc:
                query_dict[term].append(i)  # Add the index of the document where the term appears

    print("Query Likelihood Model:")
    print(query_likelihood_ranking(query_dict, documents))
    print("\nJelinek-Mercer Smoothing:")
    print(jelinek_mercer_ranking(query_dict, documents))
    
if __name__ == "__main__":
    main()
