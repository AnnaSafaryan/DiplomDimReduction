from os import makedirs
from tqdm import tqdm
import numpy as np
import os
import sys
import json
import joblib
import torch
import torch.nn as nn
import pickle


def create_path(path):
    parts = path.split('/')
    path = '/'.join(parts[:-1])
    try:
        makedirs(path)
        print(f"{path} created.")
    except FileExistsError:
        print(f"{path} exists.")

        
def save_data(data, data_path, ids=[], ids_path=""):
  create_path(data_path)
  if ids:
    create_path(ids_path)
    json.dump(ids, open(ids_path, 'w', encoding='utf-8'))
    print(f'{len(ids)} ids are saved')
  data.to_parquet(data_path)
  print(f"{sys.getsizeof(data)} -> {os.path.getsize(data_path)}")
    
    
def load_ids(ids_path):
    return json.load(open(ids_path))
    
    
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


def load_mapping(mapping_path):
    return json.load(open(mapping_path, encoding='utf-8'))


def save_vectors(data, data_path, mapping={}, mapping_path=""):
  create_path(data_path)
  if mapping:
    create_path(mapping_path)
    json.dump(mapping, open(mapping_path, 'w', encoding='utf-8'))
  np.savez_compressed(data_path, data=data)
  print(f"{sys.getsizeof(data)} -> {os.path.getsize(data_path)}")

    
def save_vector_lists_pkl(data_list, data_path, mapping={}, mapping_path=""):
  create_path(data_path)
  if mapping:
    create_path(mapping_path)
    json.dump(mapping, open(mapping_path, 'w', encoding='utf-8'))
  pickle.dump(data_list, open(data_path, 'wb'))
  print(f"{sys.getsizeof(data_list)} -> {os.path.getsize(data_path)}")
    
    
def save_vector_lists_npz(data_list, data_path, mapping={}, mapping_path=""):
  create_path(data_path)
  if mapping:
    create_path(mapping_path)
    json.dump(mapping, open(mapping_path, 'w', encoding='utf-8'))
  np.savez_compressed(data_path, data=np.array(data_list, dtype=object))
  print(f"{sys.getsizeof(data_list)} -> {os.path.getsize(data_path)}")
    
    
def load_vector_lists(vector_path): 
    return np.load(vector_path, allow_pickle=True)["data"]


def load_vectors(vector_path):
    try:
        vectors = np.load(vector_path)["data"]
    except ValueError:
        vectors = np.vstack(load_vector_lists(vector_path))
    return vectors
    
    
def save_sk_model(model, model_path):
  create_path(model_path)
  joblib.dump(model, model_path)
  print(f"{sys.getsizeof(model)} -> {os.path.getsize(model_path)}")


def load_sk_model(model_path):
    return joblib.load(model_path)


def save_ae_model(model, model_path):
  create_path(model_path)
  torch.save(model.state_dict(), model_path)
  print(f"{sys.getsizeof(model)} -> {os.path.getsize(model_path)}")


class LinearAutoencoder(nn.Module):
    def __init__(self, input_dim, output_dim, dropout_rate=0.1):
        self.__name__ = "LinearAutoEncoder"
        super(LinearAutoencoder, self).__init__()
        self.encoder = nn.Linear(input_dim, output_dim)
        self.dropout = nn.Dropout(dropout_rate)
        self.decoder = nn.Linear(output_dim, input_dim)

    def forward(self, x):
        encoded = self.encoder(x)
        encoded = self.dropout(encoded)
        decoded = self.decoder(encoded)
        return encoded, decoded
    
    
class Autoencoder(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim=None, dropout_rate=0.1):
        if not hidden_dim:
            hidden_dim = (input_dim + output_dim)//2
        self.__name__ = f"AutoEncoder{hidden_dim}"
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout_rate),
            nn.Linear(hidden_dim, output_dim),
        )
        self.decoder = nn.Sequential(
            nn.Linear(output_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, input_dim),
        )
        
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return encoded, decoded

    
def save_metrics(metrics, metrics_path):
    create_path(metrics_path)
    json.dump(metrics, open(metrics_path, "w", encoding="utf-8"))
    print(f"{sys.getsizeof(metrics)} -> {os.path.getsize(metrics_path)}")
    
def load_metrics(metrics_path):
    return json.load(open(metrics_path, encoding="utf-8"))


def save_preds(preds, preds_path):
    create_path(preds_path)
    json.dump(preds, open(preds_path, "w", encoding="utf-8"), indent=4)
    print(f"{sys.getsizeof(preds)} -> {os.path.getsize(preds_path)}")

def load_preds(preds_path):
    return json.load(open(preds_path, encoding="utf-8"))
