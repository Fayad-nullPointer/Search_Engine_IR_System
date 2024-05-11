def jaccard_similarity(query, document):
    query_set = set(query.keys())  # ** Convert query keys to a set
    document_set = set(document.keys())  # ** Convert document keys to a set

    #~~~~~~~~~! Calculate the intersection of the query set and document set !~~~~~~~~~#
    intersection = query_set.intersection(document_set)

    #~~~~~~~~~! Calculate the union of the query set and document set !~~~~~~~~~#
    union = query_set.union(document_set)

    #~~~~~~~~~! Calculate the Jaccard similarity coefficient !~~~~~~~~~#
    similarity = len(intersection) / len(union)

    return similarity

#~~~~~~~~~! Define the query and document !~~~~~~~~~#
query = {'hello': [1], 'world': [2]}
document = [{'i': [0], 'love': [1], 'comput': [1], 'scinc': [1], 'and': [2], 'deep': [1], 'learn': [1], 'ai': [1]},
            {'i': [0], 'love': [1], 'comput': [1], 'scinc': [1], 'and': [2], 'deep': [1], 'learn': [1], 'ai': [1]},
            {'hello': [1], 'world': [1]}
            ]

#~~~~~~~~~! Calculate Jaccard similarity for each document !~~~~~~~~~#
for i, doc in enumerate(document):
    similarity = jaccard_similarity(query, doc)
    print(f"Similarity between query and document {i+1}: {similarity}")