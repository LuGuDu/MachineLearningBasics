import numpy as np
import pandas as pd

# Convertir un DataFrame de Panda a un Array de Numpy

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
print(df['Fare'].values)  # Array unidimensional

# ahora tenemos varias columnas

print(df[['Pclass', 'Fare', 'Age']].values)

# Atributo Shape de Numpy: Determina el tamaño del array
# Cuantas filas y columnas tiene

arr = df[['Pclass', 'Fare', 'Age']].values  # => [ [...], [...], [...] ]
print(arr.shape)  # (887, 3)
print(df.shape)  # tambien aplicable a DataFrames de Pandas

print(arr[0, 1])  # fila 1, columna 2
print(arr[0]) # fila 1
print(arr[:, 2])  # Todos los datos de una columna especifica

# Enmascaramiento

mask = arr[:, 2] < 18  # Array de booleans que indican si se cumple o no
print(mask)  # Falso - adultos; True - niños
print(arr[mask])  # Solo imprime los que sean true (edad menor de 18)
# print(arr[arr[:, 2] < 18])

#Sumando y contando

print(mask.sum()) #Recuento valores a True