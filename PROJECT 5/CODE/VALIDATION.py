# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# %% [Markdown]


# THE MODULE

model = KNeighborsClassifier(n_neighbors=1)
iris = load_iris()
X = iris.data
y = iris.target

model.fit(X, y)
y_model = model.predict(X)

accuracy_score(y, y_model)

# split the data with 50% in each set
X1, X2, y1, y2 = train_test_split(X, y, random_state=0,
                                  train_size=0.5)

# fit the model on one set of data
model.fit(X1, y1)

# evaluate the model on the second set of data
y2_model = model.predict(X2)
accuracy_score(y2, y2_model)

# %%
