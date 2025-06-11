import numpy as np

# embeddings = np.empty([10, 3])
# lens = [3, 1, 6]  # длины вставляемых частей
# vecs = [np.random.random((l, 3)) for l in lens]  # создаём массивы

# start_point = 0
# for i, v in enumerate(vecs):
#     end_point = start_point + v.shape[0]
#     print(f"Inserting vec {i+1} of shape {v.shape}: {start_point}:{end_point}")
#     embeddings[start_point:end_point] = v
#     start_point = end_point
#
# print()
# print(embeddings)
# print()

# embeddings = np.vstack(vecs)
#
# def split_embeddings(embeddings, lens):
#     # вычисляем кумулятивные суммы, чтобы знать, где резать
#     split_indices = np.cumsum(lens[:-1])  # Не включаем последний, иначе будет выход за границу
#     return np.split(embeddings, split_indices)
#
# splits = split_embeddings(embeddings, lens)
#
# for i, s in enumerate(splits):
#     print(f"Part {i}: shape = {s.shape}")
#     print(s)


def inner(a = 1):
    print(a)

def outer(fn, kwargs_one, kwargs_two):
    fn(**kwargs_one)
    fn(**kwargs_two)

# outer(inner, {'a': 2}, {'a': 5})


for i in range(0, 21, 16):
    print(i)