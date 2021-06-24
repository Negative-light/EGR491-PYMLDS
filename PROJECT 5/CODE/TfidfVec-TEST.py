# %%

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
f = open(
    '..\CODE\INPUT\COUNTVEC_TEST.txt', 'r')
content = f.read()
content = str.split(content, '>')
cv = TfidfVectorizer()
fit = cv.fit_transform(content)
wordBYword = pd.DataFrame(fit.toarray(), columns=cv.get_feature_names())
print(wordBYword)

# %%
