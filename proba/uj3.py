import pandas as pd
import numpy as np
import sys
print(1)

a=[]
for i in range(3):
  a.append(i)
print(a)

df_0=pd.DataFrame(data={'a':[],
                      'b': [],
                      'a+b^2':[]})
df=pd.DataFrame(columns=['num','fib'])

print(df)

#append, pd.concat, pd.merge, pd.join
df=pd.DataFrame(columns=['n','fib'])
row1={'n':1.0,'fib':1.0}
row2={'n':1.0,'fib':1.0}
#df.append({'n':1, 'fib':1},ignore_index=True) #mindkét dataframe-nekk volt indexe, újat csinál
new_df=pd.DataFrame([row1,row2])
df=pd.concat([df,new_df],axis=0,ignore_index=True)
print(df.dtypes) #adattípus
#print(df)

df2=pd.DataFrame(range(1,21),columns=['n']) #1-20
df2['fib']=np.nan

df2.loc[df2["n"]==1, 'fib']=1

print(df2)
#sys.exit
fib_lag1 = 0
fib_lag2 = 0

for ix, row in df2.iterrows(): #indexet és row-t dob vissza
  #print(ix, row)

    n = row['n']

    if ix in [0,1]:
      df2.loc[ix, "fib"] = 1

    else:
        df2.loc[ix, "fib"] = df2.loc[ix-1, "fib"] + df2.loc[ix-2, "fib"]

import sys
sys.exit()

# 3 paramétere van a classnak,

class klassz():

    def __init__(self, n_rows, n_cols):
        self.value = 0

    def calculate(self):







a = velszamok (5,2)
print(a.value)