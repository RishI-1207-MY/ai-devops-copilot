import faiss
import numpy as np
import os
import json

DOC_FILE = "documents.json"
INDEX_FILE = "logs.index"

# Load saved documents
if os.path.exists(DOC_FILE):
    with open(
        DOC_FILE,
        "r",
        encoding="utf-8"
    ) as f:
        documents = json.load(f)
else:
    documents = []

# Load saved FAISS index
if os.path.exists(INDEX_FILE):
    index = faiss.read_index(INDEX_FILE)
else:
    index = faiss.IndexFlatL2(384)

def add_document(text, embedding):

    global documents

    documents.append(text)

    index.add(
        np.array(embedding).astype("float32")
    )

    # Save FAISS index
    faiss.write_index(
        index,
        INDEX_FILE
    )

    # Save documents
    with open(
        DOC_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            documents,
            f,
            ensure_ascii=False,
            indent=2
        )