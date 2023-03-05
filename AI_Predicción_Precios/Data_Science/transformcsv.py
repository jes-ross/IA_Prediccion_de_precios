'''
Jesús Rosales Santana
05-03-2023
Haré transformaciones del dataframe pues este tiene ',' y con estas no puedo hacer calculos, aparte tambien tiene 'k' y '%'.
'''
import pandas as pd #Con esta librería manejaré los datos a transformar.
import numpy as np #Con la librería numpy trataré de manerá óptima los datos. Pues pandas necesita de esta.

df = pd.read_csv('Datostotales.csv')#Con este comando leo el csv.
df.drop([ '% var.', 'Vol.'], axis = 'columns', inplace=True)#Con este comando borro las columnas que no necesito.
#Defino las listas a rellenar.
new_df = []
new2_df = []
new3_df = []
new4_df = []

'''Aquí lo que haré será con bucles for recorrer las columnas y hacer las operaciones 
de cambio y append'''

for item in df['Último']:
    if ',' in item:
        item = item.replace(',', '.')
        new_df.append(item)
for item2 in df['Apertura']:
    if ',' in item2:
        item2 = item2.replace(',', '.')
        new2_df.append(item2)
for item3 in df['Máximo']:
    if ',' in item3:
        item3 = item3.replace(',', '.')
        new3_df.append(item3)
for item4 in df['Mínimo']:
    if ',' in item4:
        item4 = item4.replace(',', '.')
        new4_df.append(item4)

#Aquí lo que hago es cambiar los valores con los nuevos datos de la transformación.
df['Último'] = new_df 
df['Apertura'] = new2_df
df['Máximo'] = new3_df
df['Mínimo'] = new4_df
#Transformando a float.
df['Último'] = df['Último'].astype(float)
df['Apertura'] = df['Apertura'].astype(float)
df['Máximo'] = df['Máximo'].astype(float)
df['Mínimo'] = df['Mínimo'].astype(float)
#Convirtiendo a csv.
df.to_csv('DatosTransformados.csv', header=True, index=False)









