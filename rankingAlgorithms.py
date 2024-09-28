import os
import math

def getAllTextDocuments():
    documents = []
    for file in os.listdir("documents"):
        if file.endswith(".txt"):
            with open(f"documents/{file}", "r") as f:
                documents.append((file, f.read()))
    return documents


def TermFrequency(query, document_content):
    words = document_content.split()
    query_count = words.count(query)
    return query_count / len(words) if len(words) > 0 else 0


def InverseDocumentFrequency(query, documents):
    num_docs_containing_query = sum(1 for _, doc_content in documents if query in doc_content)
    if num_docs_containing_query == 0:
        return 0
    return math.log(len(documents) / num_docs_containing_query)


def TFIDF(query, document_content, documents):
    tf = TermFrequency(query, document_content)
    idf = InverseDocumentFrequency(query, documents)
    return tf * idf


if __name__ == "__main__":
    documents = getAllTextDocuments()
    query = "for"
    found_in_documents = []
    
    for doc_name, doc_content in documents:
        tf = TermFrequency(query, doc_content)
        tfidf = TFIDF(query, doc_content, documents)

        if tf > 0:
            found_in_documents.append(doc_name)
            print(f"Document '{doc_name}': TF = {tf}, TF-IDF = {tfidf}")
    
    if found_in_documents:
        print("\nQuery found in the following documents:")
        for doc_name in found_in_documents:
            print(f"- {doc_name}")
    else:
        print("\nQuery not found in any documents.")
