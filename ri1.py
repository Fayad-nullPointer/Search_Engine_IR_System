def evaluate_system(ground_truth, retrieved_documents):
    precision = {}  
    recall = {}  
    f_measure = {}  
    rank_power = {}  

    for query_id, relevant_docs in ground_truth.items():
        retrieved_docs = retrieved_documents.get(query_id, [])

        retrieved_and_relevant = [doc for doc in retrieved_docs if doc in relevant_docs]
        precision[query_id] = len(retrieved_and_relevant) / len(retrieved_docs) if len(retrieved_docs) > 0 else 0

        recall[query_id] = len(retrieved_and_relevant) / len(relevant_docs) if len(relevant_docs) > 0 else 0

        if precision[query_id] + recall[query_id] > 0:
            f_measure[query_id] = (2 * precision[query_id] * recall[query_id]) / (precision[query_id] + recall[query_id])
        else:
            f_measure[query_id] = 0

        rank_power[query_id] = sum((len(relevant_docs) - relevant_docs.index(doc)) / len(relevant_docs)
                                    for doc in retrieved_docs if doc in relevant_docs)

    return precision, recall, f_measure, rank_power

def main():
    ground_truth = {}
    retrieved_documents = {}
    while True:
        query = input("Enter query as string (or type 'done' to finish): ")
        if query.lower() == 'done':
            break
        relevant_docs_input = input("Enter relevant documents (comma-separated) or type 'done' to skip: ")
        if relevant_docs_input.lower() == 'done':
            break
        retrieved_docs_input = input("Enter retrieved documents (comma-separated) or type 'done' to skip: ")
        if retrieved_docs_input.lower() == 'done':
            break
        ground_truth[query] = relevant_docs_input.split(',')
        retrieved_documents[query] = retrieved_docs_input.split(',')

    precision, recall, f_measure, rank_power = evaluate_system(ground_truth, retrieved_documents)
    print("\nResults:")
    print("Precision:", precision)
    print("Recall:", recall)
    print("F-measure:", f_measure)
    print("Rank Power:", rank_power)

if __name__ == "__main__":
    main()



