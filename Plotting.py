import pandas as pd
import matplotlib.pyplot as plt
# Libreria para mostrar los datos

pd.options.display.max_columns = 6

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

# Primer argumento, eje X
# Segundo argumento, eje Y
# El tercer parametro se utiliza para colorear los valores segun otro valor
# en este caso si es de primera, segunda o tercera clase
plt.scatter(df['Age'], df['Fare'], c=df['Pclass']) # scatter para mostrar datos

#Poner titulos a los ejes
plt.xlabel('Age')
plt.ylabel('Fare')

plt.plot([0, 80], [85, 5]) #Dibuja una linea manualmente

plt.show() # MOSTRAR EL GRAFICO
