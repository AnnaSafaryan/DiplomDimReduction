from os import makedirs
from tqdm import tqdm
import numpy as np
import os
import sys
from json import dump as jdump, load as jload
from joblib import dump, load
import torch
import pickle


def create_path(path):
    parts = path.split('/')
    path = '/'.join(parts[:-1])
    try:
        makedirs(path)
        print(f"{path} created.")
    except FileExistsError:
        print(f"{path} exists.")


def normalize(X, axis=None, eps=1e-10):
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


def create_mapping(unique_data):
  mapping = {'i2text': {}, 'text2i': {}}
  for i, elem in enumerate(unique_data):
    mapping['i2text'][i] = elem
    mapping['text2i'][elem] = i
  return mapping


def save_vectors(data, data_path, mapping={}, mapping_path=""):
  create_path(data_path)
  if mapping:
    create_path(mapping_path)
    jdump(mapping, open(mapping_path, 'w', encoding='utf-8'))
  np.savez_compressed(data_path, data=data)
  print(f"{sys.getsizeof(data)} -> {os.path.getsize(data_path)}")

    
def save_vector_lists_pkl(data_list, data_path, mapping={}, mapping_path=""):
  create_path(data_path)
  if mapping:
    create_path(mapping_path)
    jdump(mapping, open(mapping_path, 'w', encoding='utf-8'))
  pickle.dump(data_list, open(data_path, 'wb'))
  print(f"{sys.getsizeof(data_list)} -> {os.path.getsize(data_path)}")
    
    
def save_vector_lists_npz(data_list, data_path, mapping={}, mapping_path=""):
  create_path(data_path)
  if mapping:
    create_path(mapping_path)
    jdump(mapping, open(mapping_path, 'w', encoding='utf-8'))
  np.savez_compressed(data_path, data=np.array(data_list, dtype=object))
  print(f"{sys.getsizeof(data_list)} -> {os.path.getsize(data_path)}")
    

def load_vectors(vector_path):
    try:
        vectors = np.load(vector_path)["data"]
    except ValueError:
        vectors = np.load(vector_path, allow_pickle=True)["data"]
        vectors = np.vstack(vectors)
    return vectors
    
    
def save_sk_model(model, model_path):
  create_path(model_path)
  dump(model, model_path)
  print(f"{sys.getsizeof(model)} -> {os.path.getsize(model_path)}")


def save_ae_model(model, model_path):
  create_path(model_path)
  torch.save(model.state_dict(), model_path)
  print(f"{sys.getsizeof(model)} -> {os.path.getsize(model_path)}")