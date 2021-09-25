import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../data/pokemon.csv')
df.info()

# a. La media, moda y la desviación estándar por columna; explique qué significa en cada caso mediante Python sin uso de librerías

# Media
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
    datos.dropna(inplace=True)
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
media_Total = media(df.Total)
media_HP = media(df.HP)
media_Atq = media(df.Attack)
media_Def = media(df.Defense)
media_VelAtq = media(df['Sp. Atk'])
media_VelDef = media(df['Sp. Def'])
media_Vel = media(df.Speed)

#Modas
moda_Tipo1 = moda(df['Type 1'])
moda_Tipo2 = moda(df['Type 2'])
moda_Total = moda(df.Total)
moda_HP = moda(df.HP)
moda_Atq = moda(df.Attack)
moda_Def = moda(df.Defense)
moda_VelAtq = moda(df['Sp. Atk'])
moda_VelDef = moda(df['Sp. Def'])
moda_Vel = moda(df.Speed)

#Mediana
mediana_Total = mediana(df.Total)
mediana_HP = mediana(df.HP)
mediana_Atq = mediana(df.Attack)
mediana_Def = mediana(df.Defense)
mediana_VelAtq = mediana(df['Sp. Atk'])
mediana_VelDef = mediana(df['Sp. Def'])
mediana_Vel = mediana(df.Speed)

#Desviacion estandar
desviacion_Total = desv_est(df.Total)
desviacion_HP = desv_est(df.HP)
desviacion_Atq = desv_est(df.Attack)
desviacion_Def = desv_est(df.Defense)
desviacion_VelAtq = desv_est(df['Sp. Atk'])
desviacion_VelDef = desv_est(df['Sp. Def'])
desviacion_Vel = desv_est(df.Speed)

# b. La media, la moda, la desviación estándar con el uso de numpy y pandas

#Pandas
media_pandas=df.mean()
moda_pandas=df.mode()
mediana_pandas=df.median()
desviacion_pandas=df.std()

#Numpy
data_frame_n=df.to_numpy()
numericos=data_frame_n[:,4:11]
literales=data_frame_n[:,2:4]

media_numpy=np.mean(numericos,axis=0)
mediana_numpy=np.median(numericos,axis=0)
#desviacion_numpy=np.std(numericos,axis=0)
desviacion_numpy=np.power(np.var(numericos,axis=0),1/2)

# c. Grafique los datos y explique su comportamiento (PYTHON)
aux=df.mode().to_numpy()
modas_numpy=aux[0,4:11]
N = 7
ind = np.arange(N)
width = 0.2

fig,ax = plt.subplots()

x1 = ax.bar(ind, media_numpy, width)
x2 = ax.bar(ind+width, modas_numpy, width)
x3 = ax.bar(ind+width*2, mediana_numpy, width)
x4 = ax.bar(ind+width*3, desviacion_numpy, width)

ax.set_ylabel('Poder')
ax.set_title('Stats Pokemon')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels( ('Total', 'HP', 'Atq', 'Def', 'Vel. Atq', 'Vel. Def', 'Vel') )

ax.legend( (x1[0], x2[0], x3[0], x4[0]), ('Media', 'Moda','Mediana','Desviación Estandar') )
plt.show()

