# %%
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
f = open(
    '..\CODE\INPUT\COUNTVEC_TEST.txt', 'r')
content = f.read()
content = str.split(content, '>')
cv = CountVectorizer()
fit = cv.fit_transform(content)
wordBYword = pd.DataFrame(fit.toarray(), columns=cv.get_feature_names())
# %% VECTORIZE BY 2-5 WORD SEQUENCE
cv2 = CountVectorizer(ngram_range=(2, 5), analyzer='word')
fit = cv2.fit_transform(content)
twoToFive = pd.DataFrame(fit.toarray(), columns=cv2.get_feature_names())
print(wordBYword)
print(twoToFive)

# %%
