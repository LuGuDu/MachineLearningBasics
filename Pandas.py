import pandas as pd

#------------------------------
#READIN DATA WITH PANDAS
#------------------------------

pd.options.display.max_columns = 6

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
#df es nuestro objeto dataframe de pandas

print(df.head()) #devuelve las primeras 5 filas

print(df.describe()) #devuelve una tabla de estadisticas

# Count: This is the number of rows that have a value. In our case, every passenger has a value for each of the columns, so the value is 887 (the total number of passengers).
# Mean: Recall that the mean is the standard average.
# Std: This is short for standard deviation. This is a measure of how dispersed the data is.
# Min: The smallest value
# 25%: The 25th percentile
# 50%: The 50th percentile, also known as the median.
# 75%: The 75th percentile
# Max: The largest value


#------------------------------
#MANIPULATING DATA WITH PANDAS
#------------------------------

col = df['Fare'] #seleccionar una columna
#El resultado es llamado 'Pandas Series', como un DF pero solo con una unica columna
print(col)

small_df = df[['Age', 'Sex', 'Survived']] #hay que usar doble [] para multiples columnas
print(small_df.head())

#Creating a column
print(df['Sex'] == 'male')
#creamos una columna con los resultados
df['Male'] = df['Sex'] == 'male'
print(df.head())
