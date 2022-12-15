import pandas as pd
df=pd.read_csv('main.csv')
del df['Star Name']
del df['Distance (ly)']
del df['Mass(MJ)']
del df['Radius (RJ)']
print(df.shape)
print(list(df))
df = df.dropna()
df.to_csv('main2.csv')