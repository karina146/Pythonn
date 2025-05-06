import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter = ',', dtype = 'object')
species = iris[:, -1]
unique, count = np.unique(species, return_counts = True)

for i in range(len(unique)):
    print(f'{unique[i]}: {count[i]}')