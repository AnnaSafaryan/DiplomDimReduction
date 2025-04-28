from os import makedirs
import numpy as np


def create_path(path):
    parts = path.split('/')
    path = '/'.join(parts[:-1])
    try:
        makedirs(path)
        print(f"{path} created.")
    except FileExistsError:
        print(f"{path} exists.")


def normalize(X, axis=None, eps=1e-10):
    # X = np.asarray(X)
    if X.ndim == 1:
        norm = np.linalg.norm(X, ord=2)
        return X / (norm + eps)
    elif X.ndim == 2:
        norm = np.linalg.norm(X, ord=2, axis=1 if axis is not None else 1, keepdims=True)
        return X / (norm + eps)
    else:
        raise ValueError("Input must be a 1D or 2D array.")


def cosine_similarity(vec, matrix):
  return normalize(matrix, axis=1) @ normalize(vec).T