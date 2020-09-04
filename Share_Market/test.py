import requests
import lxml.html as lh
import pandas as pd
import json

from nsetools import Nse
nse = Nse()
data = nse.get_preopen_nifty(as_json=True)
#print(data)
data = json.loads(data)
# print(type(data))
# print(data[0])
# for k,v in data[0].items():
#     print(k,v)
# print(pd.Series(data))
#print(data)

df = pd.DataFrame(data)
#print(df.head(2))
#print(df.columns)
#print(df[['symbol', 'iep', 'pCls', 'chn','perChn']])
#print(df[float(df['perChn']) > 1.0])
df['perChn'] = df['perChn'].astype(float)
#print(df)
df = df[df['perChn'] > 1.0]
print(df[['symbol', 'iep', 'pCls', 'chn','perChn']])


#print(df[['symbol', 'iep', 'pCls', 'chn','perChn']][df[df['perChn'] > 1.0]])


