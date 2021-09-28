import pandas as pd
from sklearn import preprocessing  

df = pd.read_csv('../data/vgsales.csv')

num=df[['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
print("-------------------------------------------------------------------------------------------------")
print("Data Frame")
print(df.head())

# Normalización
aux = preprocessing.normalize(num)
dfnorm=df.copy()
dfnorm['NA_Sales']=aux[:,0]
dfnorm['EU_Sales']=aux[:,1]
dfnorm['JP_Sales']=aux[:,2]
dfnorm['Other_Sales']=aux[:,3]
dfnorm['Global_Sales']=aux[:,4]
dfnorm.head()
print("-------------------------------------------------------------------------------------------------")
print("Data Frame Normalizado")
print(dfnorm.head())

# Discretización
est = preprocessing.KBinsDiscretizer(n_bins=10, encode='ordinal').fit(num)
aux1=est.transform(num)
dfdisc=df.copy()

dfdisc['NA_Sales']=aux1[:,0]
dfdisc['EU_Sales']=aux1[:,1]
dfdisc['JP_Sales']=aux1[:,2]
dfdisc['Other_Sales']=aux1[:,3]
dfdisc['Global_Sales']=aux1[:,4]
dfdisc.head()
print("-------------------------------------------------------------------------------------------------")
print("Data Frame Discretizado")
print(dfdisc.head())

#Estandarizacion
scaler = preprocessing.StandardScaler().fit(num)
dfst=df.copy()
aux2 = scaler.transform(num)
dfst['NA_Sales']=aux2[:,0]
dfst['EU_Sales']=aux2[:,1]
dfst['JP_Sales']=aux2[:,2]
dfst['Other_Sales']=aux2[:,3]
dfst['Global_Sales']=aux2[:,4]
dfst.head()
print("-------------------------------------------------------------------------------------------------")
print("Data Frame Estandarizado")
print(dfst.head())