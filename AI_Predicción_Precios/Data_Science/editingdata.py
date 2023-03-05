import pandas as pd #Con la libreria pandas manejare todos los datos a tratar, concatenar, eliminar, etc.
import numpy as np #Con esta libreria lograremos un correcto funcionamiento de pandas ademas de poder hacer distintas operaciones matemáticas.
import os #Con esta librería buscaremos los ficheros dentro del ordenador.
import glob #Con esta libreria crearé un fichero CSV en base a los que descargué desde Investing.com. 
'''Los ficheros CSV descargados desde Investing.com son
AUD_USD, EUR_GBP, EUR_JPY, EUR_USD, GBP_USD, NZD_USD, USD_BRL, USD_CAD, USD_JPY, USD_MXN;
tosdos estos son pares de divisas con las que entrenaré al algoritmo.
'''

all_files = glob.glob("C:/Users/Usuario/Desktop/AI_Predicción_Precios/Data_Science/Datosmonedas/*.csv")#Con este comando se recorre la ruta deseada de los archivos a transformar.

file_list = [] #Se crea una variable para añadir los datos transformados.

for f in all_files:#Se recorrera con un bucle toda la carpeta y se leerá el contenido de los archivos.
    data = pd.read_csv(f)
    name = os.path.basename(f)#Se busca el nombre.
    data['source_file'] = name #Se añadira una columna al dataframe para así comprobar que todo esta bien.
    file_list.append(data)#Se añaden los datos a la variable.

df = pd.concat(file_list, ignore_index=True)#Se concatenan los dataframes y se crea un nuevo indice.
print(df)
df.to_csv('Datostotales.csv', header=True, index=False)