# %%
# ALL THE IMPORTS
# IMPORTS
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
