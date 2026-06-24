import numpy as np

from rag.embeddings import get_embedding
from rag.vector_store import index, documents

def search_logs(query, k=3):

    if len(documents) == 0:
        return ["No logs have been indexed yet"]

    query_vector = get_embedding(query)

    distances, indices = index.search(
        np.array(query_vector).astype("float32"),
        min(k, len(documents))
    )

    results = []

    for idx in indices[0]:

        if idx >= 0 and idx < len(documents):

            results.append(
                documents[idx]
            )

    return results