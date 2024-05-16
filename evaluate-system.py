def evaluate_system(query, documents):
    #~~~~~~~~~! Calculate the total number of relevant documents !~~~~~~~~~#
    total_relevant_docs = len(documents)

    #~~~~~~~~~! Initialize variables for precision, recall, and relevant documents found !~~~~~~~~~#
    precision = 0
    recall = 0
    relevant_found = 0

    for doc in documents:
    #~~~~~~~~~! Calculate the intersection between the query and the document !~~~~~~~~~#
        intersection = set(query.keys()).intersection(set(doc.keys()))

    #~~~~~~~~~! Calculate precision and recall !~~~~~~~~~#
        precision += len(intersection) / len(doc)
        recall += len(intersection) / len(query)

        
        if len(intersection) > 0: # ** Check if the document is relevant
            relevant_found += 1

    #~~~~~~~~~! Calculate precision, recall, and F-measure !~~~~~~~~~#
    if len(documents) > 0:
        precision /= len(documents)
        recall /= len(documents)

    if precision + recall > 0:
        f_measure = (2 * precision * recall) / (precision + recall)
    else:
        f_measure = 0

    #~~~~~~~~~! Calculate rank power !~~~~~~~~~#
    if total_relevant_docs > 0:
        rank_power = relevant_found / total_relevant_docs
    else:
        rank_power = 0

    #~~~~~~~~~! Print the evaluation results !~~~~~~~~~#
    print("Evaluation Results:")
    print("Precision:", precision)
    print("Recall:", recall)
    print("F-measure:", f_measure)
    print("Rank Power:", rank_power)

#~~~~~~~~~! Test the evaluate_system function !~~~~~~~~~#
query = {'hello': [1], 'world': [2]}
documents = [{'i': [0], 'love': [1], 'comput': [1], 'scinc': [1], 'and': [2], 'deep': [1], 'learn': [1], 'ai': [1]},
             {'i': [0], 'love': [1], 'comput': [1], 'scinc': [1], 'and': [2], 'deep': [1], 'learn': [1], 'ai': [1]}]

evaluate_system(query, documents)