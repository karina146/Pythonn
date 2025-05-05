import numpy as np


a = []
f = open('matrix.txt', 'r').readlines()
for i in f:
    t = [int(j) for j in i.split(',')]
    a.append(t)
matr = np.array(a, dtype='int')
print(matr)

print(f"sum: {np.sum(matr)}")
print(f"max: {np.max(matr)}")
print(f"min: {np.min(matr)}")