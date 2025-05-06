import numpy as np
import scipy.linalg as ln
import scipy.stats as st
import time

def log_multivariate_normal(x, m, c):
    n, d, = x.shape
    c_inv = ln.inv(c)
    c_det = ln.det(c)
    const = -0.5 * d * np.log(2 * np.pi) - 0.5 * np.log(c_det)
    log = np.zeros(n)
    for i in range(n):
        diff = x[i] - m
        log[i] = const - 0.5 * np.dot(diff.T, np.dot(c_inv, diff))
    return log


n = int(input())
d = int(input())

x = np.random.rand(n, d)
m = np.random.rand(d)
c = np.random.rand(d, d)
c = np.dot(c, c.T)


start_time = time.time()
log_function = log_multivariate_normal(x, m, c)
function_time = time.time() - start_time

start_time = time.time()
log_scipy = st.multivariate_normal(m, c).logpdf(x)
scipy_time = time.time() - start_time

print(f"log_multivariate_normal: {function_time}")
print(f"multivariate_normal: {scipy_time}")
print(log_function)
print(log_scipy)
