# %%

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from numpy import nan
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer

data_main = np.array([[nan, 0,   3],
                      [3,   7,   9],
                      [nan,   5,   nan],
                      [4,   nan, 6],
                      [nan,   8,   1],
                      [1, 1, 1],
                      [3, 4, 9]])
imp = SimpleImputer(strategy='mean')
data_mean = imp.fit_transform(data_main)
imp = SimpleImputer(strategy='median')
data_median = imp.fit_transform(data_main)
imp = SimpleImputer(strategy='most_frequent')
data_freq = imp.fit_transform(data_main)
imp = SimpleImputer(strategy='constant', fill_value=2)
data_const = imp.fit_transform(data_main)
imp = KNNImputer(n_neighbors=3)
data_KNN = imp.fit_transform(data_main)
# %%
print(data_main)
print('--------------')
print(data_mean)
print('--------------')
print(data_median)
print('--------------')
print(data_freq)
print('--------------')
print(data_const)
print('--------------')
print(data_KNN)

# %%
sns.set()
plt.scatter(data_main[:, 0], data_main[:, 1],
            marker='v', label='Actual', s=200)
plt.scatter(data_mean[:, 0], data_mean[:, 1],
            alpha=0.75, label='Mean', marker='^')
plt.scatter(data_median[:, 0], data_median[:, 1],
            alpha=0.75, label='Median', marker='s')
plt.scatter(data_freq[:, 0], data_freq[:, 1],
            alpha=0.75, label='Frequent', marker='d')
plt.scatter(data_main[:, 0], data_main[:, 1], marker='.',
            label='Const', edgecolors='red', facecolors='none', s=200)
plt.scatter(data_KNN[:, 0], data_KNN[:, 1],
            marker='p', label='KNN')

plt.legend()

plt.savefig('..\images\IMPUTATION.jpg')

# %%
