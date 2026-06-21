import faiss
import numpy as np

dimension = 384

index = faiss.IndexFlatL2(
    dimension
)

documents = []

def add_document(
    embedding,
    text
):

    global documents

    index.add(
        np.array(embedding)
    )

    documents.append(text)