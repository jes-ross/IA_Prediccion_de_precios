'''
Jesús Rosales Santana
05-03-2023
Modelo Machine Learning de Regresión Lineal
'''
import numpy as np#Librería para hacer calculos.
import pandas as pd#Librería para gestión de datos.
from sklearn.linear_model import LinearRegression#Librería con la que se entrenará el modelo. 

df = pd.read_csv('DatosTransformados.csv')#Para leer el dataframe. 
#Defino las columnas.
X = df[['Apertura']]
Y = df['Último']
#Para obtener los valores de las columnas
X = X.values

reg = LinearRegression()#Así se inicia el modelo.
reg.fit(X, Y)
reg.predict([[1.0636]])