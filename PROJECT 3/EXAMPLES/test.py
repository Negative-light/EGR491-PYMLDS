import pandas as pd
import numpy as np

s1 = pd.Series(np.arange(33))
s2 = pd.Series(np.random.randint(0,100,33))
df = pd.DataFrame({'s1':s1,'s2':s2})

with pd.ExcelWriter('test.xlsx') as w:
     df.to_excel(w, sheet_name='test')
     df.to_excel(w, sheet_name='test2')
print("FINISHED WRITING TO EXCEL")