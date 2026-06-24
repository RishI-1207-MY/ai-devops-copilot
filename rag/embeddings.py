import hashlib
import numpy as np

def get_embedding(text):

    h = hashlib.md5(
        text.encode()
    ).digest()

    arr = np.frombuffer(
        h,
        dtype=np.uint8
    ).astype("float32")

    arr = np.resize(arr, 384)

    return [arr]