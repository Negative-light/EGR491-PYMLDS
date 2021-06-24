# %%
# ALL THE IMPORTS
# IMPORTS
from sklearn.feature_extraction import DictVectorizer
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt  # PLOTING
import numpy as np  # NUMPY
import pandas as pd  # PANDAS
from sklearn.datasets import load_iris  # Dataset
# Models
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.linear_model import LinearRegression
# LOAD IRIS DATA
iris = load_iris()
X = iris.data
y = iris.target

# SETUP Linear Regression model
model_1 = LinearRegression(fit_intercept=True)
x = X[:, np.newaxis]
x.shape

model_1.fit(X, y)

xfit = np.linspace(-1, 11)
Xfit = xfit[:, np.newaxis]
yfit = model_1.predict(Xfit)
print(model_1)

# %%
data = [{'power': 100, 'usage': 31, 'type': 'development'},
        {'power': 5, 'usage': 23, 'type': 'development'},
        {'power': 35, 'usegae': 37, 'type': 'gameing'}]

v = DictVecorizer(spase=False)
X = v.fit_transform(data)
print(X)
print(v.inverse_transform(X))
print(v.transform({'power': 33, 'usage': 21, 'type': 'gameing'}))

# %%
