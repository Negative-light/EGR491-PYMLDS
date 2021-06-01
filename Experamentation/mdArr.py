import numpy as np

#Regular Array
arrPy = [range(i, i+5) for i in range(1,5)]
print(arrPy)

# Numpy Array
arrNp = np.array([range(i, i+5) for i in range(1,5)])
print(arrNp)

# Boardcasting
arr1 = np.ones((3,3,3))
arr2 = np.arange(3)
arr3 = np.arange(3)[: np.newaxis]
arr2 += arr3
print(arr1 * arr2)