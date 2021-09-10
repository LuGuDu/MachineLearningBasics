import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression

cancer_data = load_breast_cancer()

print(cancer_data.keys())
# print(cancer_data['DESCR']) # Imprime la descricion

# Target: si el cancer es malicioso o benigno

# Tamaño del dataset
print(cancer_data['data'].shape)
# Almacenamos las features_names
columns = cancer_data['feature_names']
# Guardamos el dataset en un DataFrame de pandas
df = pd.DataFrame(cancer_data['data'], columns=columns)
print(df.head())

print(cancer_data['target'])
print(cancer_data['target'].shape)
# Necesitamos interpretar que significa 1 y 0, maligno o benigno.
print(cancer_data['target_names'])  # 0 maligno, 1 benigno

df['target'] = cancer_data['target']
print(df.head())

# Construimos un modelo logistico de regresion
X = df[cancer_data.feature_names].values
y = df['target'].values

# Cambiamos el algoritmo que usa el modelo para encontrar la ecuacion de la linea
# Ya que sin ese parametro tardaria mucho tiempo
model = LogisticRegression(solver='liblinear')
model.fit(X, y)
print(model.predict([X[0]])) #Maligno
print(model.score(X, y))
