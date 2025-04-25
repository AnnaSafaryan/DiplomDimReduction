import numpy as np
a = np.empty(2)
a = [np.empty(2), np.empty([3, 9])]
print(a)

np.savez_compressed('a.npz', data = np.array(a, dtype=object))

b = np.load('a.npz', allow_pickle=True)['data']
print(b)

