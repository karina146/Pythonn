import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
x0 = []
for i in x:
    if x[i] == x[0]:
        continue
    else:
        if x[i-1] == 0:
            x0.append(x[i])
print(max(x0))