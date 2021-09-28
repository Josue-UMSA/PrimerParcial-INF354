import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate #pip install tabulate

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

#Comparar datos
tablaMedia={"Datos": ["Total","HP","Atq","Def","Vel. Atq","Vel. Def","Vel"],
       "Media Manual": [media_Total, media_HP, media_Atq, media_Def, media_VelAtq, media_VelDef, media_Vel],
       "Media Pandas": [media_pandas[1],media_pandas[2],media_pandas[3],media_pandas[4],media_pandas[5],media_pandas[6],media_pandas[7]],
       "Media Numpy": [media_numpy[0], media_numpy[1], media_numpy[2], media_numpy[3], media_numpy[4], media_numpy[5], media_numpy[6]]
       }

tablaMediana={"Datos": ["Total","HP","Atq","Def","Vel. Atq","Vel. Def","Vel"],
       "Mediana Manual": [mediana_Total, mediana_HP, mediana_Atq, mediana_Def, mediana_VelAtq, mediana_VelDef, mediana_Vel],
       "Mediana Pandas": [mediana_pandas[1],mediana_pandas[2],mediana_pandas[3],mediana_pandas[4],mediana_pandas[5],mediana_pandas[6],mediana_pandas[7]],
       "Mediana Numpy": [mediana_numpy[0], mediana_numpy[1], mediana_numpy[2], mediana_numpy[3], mediana_numpy[4], mediana_numpy[5], mediana_numpy[6]]
       }

tablaModa1={"Datos": ["Total","HP","Atq","Def","Vel. Atq","Vel. Def","Vel"],
       "Moda Manual": [moda_Total, moda_HP, moda_Atq, moda_Def, moda_VelAtq, moda_VelDef, moda_Vel],
       "Moda Pandas": [moda_pandas["Total"][0],moda_pandas["HP"][0],moda_pandas["Attack"][0],moda_pandas["Defense"][0],moda_pandas["Sp. Atk"][0],moda_pandas["Sp. Def"][0],moda_pandas["Speed"][0]]
       }

tablaDesvEst={"Datos": ["Total","HP","Atq","Def","Vel. Atq","Vel. Def","Vel"],
       "Desv. Est Manual": [desviacion_Total, desviacion_HP, desviacion_Atq, desviacion_Def, desviacion_VelAtq, desviacion_VelDef, desviacion_Vel],
       "Desv. Est Pandas": [desviacion_pandas[1],desviacion_pandas[2],desviacion_pandas[3],desviacion_pandas[4],desviacion_pandas[5],desviacion_pandas[6],desviacion_pandas[7]],
       "Desv. Est Numpy": [desviacion_numpy[0], desviacion_numpy[1], desviacion_numpy[2], desviacion_numpy[3], desviacion_numpy[4], desviacion_numpy[5], desviacion_numpy[6]]
       }

tablaModa2={"Datos": ["Tipo 1", "Tipo 2"],
            "Moda Manual": [moda_Tipo1, moda_Tipo2],
            "Moda Pandas": [moda_pandas["Type 1"][0], moda_pandas["Type 2"][0]],
            }
print(tabulate(tablaMedia, headers='keys', tablefmt='fancy_grid'))
print(tabulate(tablaDesvEst, headers='keys', tablefmt='fancy_grid'))
print(tabulate(tablaMediana, headers='keys', tablefmt='fancy_grid'))
print(tabulate(tablaModa1, headers='keys', tablefmt='fancy_grid'))
print(tabulate(tablaModa2, headers='keys', tablefmt='fancy_grid'))
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

