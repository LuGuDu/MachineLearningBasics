import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
# Libreria que importa muchos algoritmos basicos de Machine Learning
# Documentacion:
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

# Convertimos a datos numericos la columna de Sex
df['male'] = df['Sex'] == 'male'

# Creamos un array numpy llamado x con las columnas que nos interesen
# features -> x
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values

# establecemos nuestro target (objetivo) en la variable y
# target -> y
y = df['Survived'].values

print(X)
print(y)

# Todos los modelos de sklearn estan construidos en clases.
model = LogisticRegression()
# ahora podemos usar los datos anteriores para entrenar al modelo
# el metodo fit(x, y) es usado para construir el modelo
# (x - numpy array 2dimensiones)
# (y - numpy array 1dimension)

X = df[['Fare', 'Age']].values
y = df['Survived'].values

model.fit(X, y)  # Con esto podemos elegir la linea que mejor se ajuste

print(model.coef_, model.intercept_)
# Con esos valores podemos formar la recta
# es decente, pero no la mejor debido a que solo hemos usado 2 features

plt.scatter(df['Fare'], df['Age'], c=df['Survived']) # scatter para mostrar datos

#Poner titulos a los ejes
plt.xlabel('Fare')
plt.ylabel('Age')

plt.plot([0, 80], [85, 5]) #Dibuja una linea manualmente

plt.show() # MOSTRAR EL GRAFICO






X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values
model = LogisticRegression()
model.fit(X, y)


#model.predict(X) podemos usarlo para predecir
# Datos del primer pasajero [3, True, 22.0, 1, 0, 7.25]
print(model.predict([[3, True, 22.0, 1, 0, 7.25]])) # [0] No sobrevive

# Ahora el modelo predecira para las primera 5 columnas
# y lo compararemos con los valores reales
print(model.predict(X[:5]))
print(y[:5])
# si imprime 1 el modelo predice que sobrevivr??, 0 que no sobrevivira


#Podemos ver como de bueno es el modelo contando el numero de predicciones correctas
#Puntuacion de precision
y_pred = model.predict(X)
print((y == y_pred).sum()) #obtiene el numero de los evaluados a True
#714 de 887

#obtenemos el porcentaje
print((y == y_pred).sum() / y.shape[0])

#El modelo hace predicciones correctas con un 80% de precision
#Sklearn tiene implementado este calculo con el metodo score(X,y)
print(model.score(X, y))


