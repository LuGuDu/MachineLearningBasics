import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix

# Accuracy, Precision, Recall y F1 Score en Sklear

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

model = LogisticRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Cada funcion toma dos arrays numpy unidimensionales:
# - Los verdaderos valores del objetivo
# - Los valores predichos del objetivo

print("accuracy:", accuracy_score(y, y_pred)) # El 80% de las predicciones son correctas
print("precision:", precision_score(y, y_pred)) # El 78% de las predicciones positivas son correctas
print("recall:", recall_score(y, y_pred)) # El 68% de los casos positivos que el modelo ha predicho correctamente
print("f1 score:", f1_score(y, y_pred)) # La media entre la precision y el recall es un 73%

'''
Con un único modelo, los valores de la métrica no nos dicen mucho. 
Para algunos problemas un valor del 60% es bueno, y para otros un 
valor del 90% es bueno, dependiendo de la dificultad del problema. 
Utilizaremos los valores métricos para comparar diferentes modelos 
y elegir el mejor. 
'''


# MATRIZ DE CONFUSION

# Con sklearn tenemos una fucion para obtener los 4 valores de la matriz
print(confusion_matrix(y, y_pred))

#IMPORTANTE: sklearn le da la vuelta a la matriz. CUIDADO A LA HORA DE INTERPRETAR LOS DATOS

'''
MATRIZ DE CONFUSION DE SKLEARN:
                           Predichos incorrectamente || Predichos correctamente
                          ---------------------------||-------------------------
Realmente incorrectos -->           TN               ||           FP
Realmente correctos ---->           FN               ||           TP

///********************************************************************************///

MATRIZ DE CONFUSION:
                               Realmente correctos || Realmente incorrectos
                               --------------------||----------------------
Predichos correctamente ---->           TP         ||          FP
Predichos incorrectamente -->           FN         ||          TN
'''