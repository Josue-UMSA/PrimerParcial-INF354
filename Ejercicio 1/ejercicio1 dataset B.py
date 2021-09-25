import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../data/vgsales.csv')
df.info()
df.dropna(how="any",inplace = True)
df.Year = df.Year.astype(int)
df.info()
df.head()
# a. La media, moda y la desviación estándar por columna; explique qué significa en cada caso mediante Python sin uso de librerías

# Media para valores numericos
def media(datos):
    suma=0
    n=len(datos.index)
    for x in datos:
        suma=suma+x
    media=suma/n
    return media
#Moda
def moda(datos):
    frecuencia={}
    for x in datos:
        frecuencia[x]=frecuencia.get(x,0)+1
    m=max(frecuencia.values())
    modas=[key for key, value in frecuencia.items()
           if value == m]
    return modas

#Mediana
def mediana(datos):
    n=len(datos.index)
    data_s=datos.sort_values(ascending=True,ignore_index=True)
    mediana=0
    if n%2 == 0:
        mediana=(data_s[n/2]+data_s[(n/2)+1])/2
    else:
        mediana=data_s[(n+1)/2]
    return mediana

#Desviacion estandar
def desv_est(datos):
    n=len(datos.index)
    xm=media(datos)
    sumatoria=0
    for x in datos:
        sumatoria=sumatoria+pow(x-xm,2)
    varianza=sumatoria/n
    desviacion=pow(varianza,1/2)
    return desviacion


# Media de las columnas
media_NA = media(df.NA_Sales)
media_EU = media(df.EU_Sales)
media_JP = media(df.JP_Sales)
media_Otros = media(df.Other_Sales)
media_Global = media(df.Global_Sales)

#Modas
moda_plataforma = moda(df.Platform)
moda_año = moda(df.Year)
moda_genero = moda(df.Genre)
moda_publisher = moda(df.Publisher)

#Mediana
mediana_NA=mediana(df.NA_Sales)
mediana_EU=mediana(df.EU_Sales)
mediana_JP=mediana(df.JP_Sales)
mediana_Otros = mediana(df.Other_Sales)
mediana_Global = mediana(df.Global_Sales)

#Desviacion estandar
desviacion_NA = desv_est(df.NA_Sales)
desviacion_EU = desv_est(df.EU_Sales)
desviacion_JP = desv_est(df.JP_Sales)
desviacion_Otros = desv_est(df.Other_Sales)
desviacion_Global = desv_est(df.Global_Sales)

# b. La media, la moda, la desviación estándar con el uso de numpy y pandas

#Pandas
media_pandas=df.mean()
moda_pandas=df.mode()
mediana_pandas=df.median()
desviacion_pandas=df.std()

#Numpy
data_frame_n=df.to_numpy()
numericos=data_frame_n[:,6:11]
literales=data_frame_n[:,2:6]
media_numpy=np.mean(numericos,axis=0)
mediana_numpy=np.median(numericos,axis=0)
#desviacion_numpy=np.std(numericos,axis=0)
desviacion_numpy=np.power(np.var(numericos,axis=0),1/2)

# c. Grafique los datos y explique su comportamiento (PYTHON)

N = 5
ind = np.arange(N)
width = 0.3

fig,ax = plt.subplots()

x1 = ax.bar(ind, media_numpy, width)
x2 = ax.bar(ind+width, mediana_numpy, width)
x3 = ax.bar(ind+width*2, desviacion_numpy, width)

ax.set_ylabel('Ventas')
ax.set_title('Ventas de Videojuegos')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels( ('NA', 'EU', 'JP', 'Otros', 'Global') )

ax.legend( (x1[0], x2[0], x3[0]), ('Media', 'Mediana','Desviación Estandar') )
plt.show()

