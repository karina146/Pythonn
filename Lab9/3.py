import numpy as np

x = np.random.normal(size=(10,4))

x5 = x[:5]
print(x)
print(x5)
print(f"mean: {np.mean(x)}")
print(f"max: {np.max(x)}")
print(f"min: {np.min(x)}")