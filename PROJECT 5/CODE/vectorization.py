# %%
from sklearn.feature_extraction import DictVectorizer
data = [{'power': 100, 'usage': 31, 'type': 'development'},
        {'power': 5, 'usage': 23, 'type': 'development'},
        {'power': 35, 'usage': 37, 'type': 'gameing'}]

v = DictVectorizer(sparse=False)
X = v.fit_transform(data)
print('----------------')
print(X)
print('----------------')
print(v.inverse_transform(X))
print('----------------')
print(v.transform({'power': 33, 'usage': 21, 'type': 'gameing'}))

# %%
