import math

def cosine_similarity(query, document):
    #~~~~~~~~~! Calculate the dot product of the query and document vectors !~~~~~~~~~#
    dot_product = 0
    for term in query:
        if term in document:
            dot_product += query[term][0] * document[term][0]

    #~~~~~~~~~! Calculate the magnitudes of the query and document vectors !~~~~~~~~~#
    query_magnitude = math.sqrt(sum([freq[0] ** 2 for freq in query.values()]))
    document_magnitude = math.sqrt(sum([freq[0] ** 2 for freq in document.values()]))

    #~~~~~~~~~! Calculate the cosine similarity of the query and document vectors !~~~~~~~~~#
    similarity = dot_product / (query_magnitude * document_magnitude)

    return round(similarity,2)

#~~~~~~~~~! Define the query and document !~~~~~~~~~#
query = {'hello': [1], 'world': [2]}
document = [{'i': [0], 'love': [1], 'comput': [1], 'scinc': [1], 'and': [2], 'deep': [1], 'learn': [1], 'ai': [1]},
            {'i': [0], 'love': [1], 'comput': [1], 'scinc': [1], 'and': [2], 'deep': [1], 'learn': [1], 'ai': [1]},
            {'hello': [1], 'world': [1]}]

#~~~~~~~~~! Calculate cosine similarity for each document !~~~~~~~~~#
for i, doc in enumerate(document):
    similarity = cosine_similarity(query, doc)
    print(f"Similarity between query and document {i+1}: {similarity}")