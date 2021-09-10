import numpy as np
import pandas as pd

#Convertir un DataFrame de Panda a un Array de Numpy

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
print(df['Fare'].values) #Array unidimensional

#ahora tenemos varias columnas

print(df[['Pclass', 'Fare', 'Age']].values)

#Atributo Shape de Numpy: Determina el tamaño del array
#Cuantas filas y columnas tiene

arr = df[['Pclass', 'Fare', 'Age']].values
print(arr.shape) #(887, 3)
print(df.shape) #tambien aplicable a DataFrames de Pandas

arr = df[['Survived', 'Pclass']].values
print(arr.shape) #(887, 2)

