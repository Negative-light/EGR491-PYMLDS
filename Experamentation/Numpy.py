import numpy as np

print(np.linspace(0, 100, 10, dtype='int'))
print("---------------------------------")
rand = np.random.RandomState(45)
X = rand.randint(0,10,(5,5,5))
print(X)
X = np.sort(X, axis=2)
print(X)
