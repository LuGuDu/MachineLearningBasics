En el módulo anterior se ha calculado como de bueno es el modelo usado
utilizando la exactitud (accurancy), el porcentaje de las predicciones que
son correctas.

P.e. si tenemos 100 datos y predecimos 70 correctamente y 30 no, la exactitud
es del 70%

La exactitud es una métrica muy sencilla y fácil de entender, pero no siempre
es la mejor. Es una buena medida si nuestras clases están divididas por igual,
pero es muy engañosa si tenemos clases desequilibradas.

Siempre hay que tener cuidado con la exactitud. Es necesario conocer la
distribución de las clases para saber como interpretar el valor.


    ---------------------
     MATRIZ DE CONFUSION
    ---------------------

Entonces, no solo tenemos que preocuparnos de los datos para los que predecimos la
clase correcta, sino también el número de datos positivos que predecimos correctamente,
asi como el número de datos negativos que predecimos correctamente.

Podemos ver todos esos valores importantes en lo que se le llama la Matriz de Confusion

La matriz de confusion es una tabla que muestra cuatro valores:
 - datos que predecimos correctamente que son realmente correctos
 - datos que predecimos correctamente que son realmente incorrectos
 - datos que predecimos incorrectamente que son realmente correctos
 - datos quu predecimos incorrectamente que son realmente incorrectos

El primer y cuarto dato son los datos que predecimos correctamente; y el segundo y tercer
dato son los que predecimos incorrectamente.


Ejemplo:

Tenemos 887 pasajeros: 342 sobrevivieron (positivo) y 545 no (negativo). Tenemos la siguiente
matriz de confusion:

                              Realmente correctos || Realmente incorrectos
                              --------------------||----------------------
Predichos correctamente ---->         233         ||          65
Predichos incorrectamente -->         109         ||          480

Los valores superior izquierdo, e inferior derecho son las predicciones correctas. Luego,
de 342 pasajeros que sobrevivieron, hemos predicho 233 correctamente (109 no). De los 545
pasajeros que no sobrevivieron, hemos predicho 480 correctamente (65 no).

Podemos usar la matriz de confusion para calcular la exactitud. Como recordatorio, la
exactitud es el número de datos que hemos predicho correctamente dividido por el total de
datos que hay.

    (233+480)/(233+65+109+480) = 713/887 = 80.38%

La matriz de confusion describe completamente el rendimiento de un modelo en un conjunto
de datos, aunque es difícil de utilizar para comparar modelos.


Cada valor de la matriz de confusion tiene un nombre:
 - True positive (TP) - dato predicho positivamente y que es correcto
 - True negative (TN) - dato predicho negativamente y que es correcto
 - False positive (FP) - dato predicho positivamente y que es incorrecto
 - False negative (FN) - dato predicho negativamente y que es incorrecto

 Para recordarlo mejor tenemos que la segunda palabra es acerca de nuestra predicción:
 positiva o negativa; y la primera palabra habla de si la predicción fue correcta o no

                               Realmente correctos || Realmente incorrectos
                               --------------------||----------------------
Predichos correctamente ---->           TP         ||          FP
Predichos incorrectamente -->           FN         ||          TN


Estos cuatro valores son utilizados para calcular diferentes métricas que se verán mas adelante



    -----------------------
     PRECISION (PRECISION)
    -----------------------

Dos métricas comunmente usadas para la clasificacion son la precisión y el recall. Conceptualmente
la precision se refiere al porcentaje de resultados positivos que son relevantes y el recall el
porcentaje de casos positivos correctamente clasificados.

Ambos valores pueden ser definidos usando los cuadrantes de la amtriz de ocnfusion.

Definimos la precision:
                # positivos predichos correctamente        TP
Precision = ----------------------------------------- = ---------
                      # predicciones correctas           TP + FP


Según el ejemplo anterior tenemos que la precision es:
    233 / (233 + 65) = 0.7819

De modo que, la precisión es una medida de la exactitud del modelo en sus predicciones positivas


    --------
     RECALL
    --------

Este valor es el porcentaje de casos positivos que el modelo predice correctamente. De nuevo, para
calcularlo podemos usar la matriz de confusion.

Definimos el recall:
             # positivos predichos correctamente        TP
recall = ----------------------------------------- = ---------
                   # casos positivos                  TP + FN

Segun el ejemplo de los supervivientes:
     233 / (233 + 109) = 0.6813

De modo que, el recall es una medida de cuantos casos positivos puede recordar el modelo.



    ---------------------------------------
     COMPENSACION ENTRE PRECISION Y RECALL
    ---------------------------------------

Normalmente nos encontraremos en la situacion de elegir entre aumentar el recall (y disminuir la precision)
o aumentar la precision (y disminuir el recall). Eso dependerá de la situación en la cual queramos maximizar
una cosa o la otra.

Por ejemplo, digamos que estamos construyendo un modelo para predecir si un cargo en la tarjeta de credito es
fraudulento. Los casos positivos para nuestro modelo son las cargas fraudulentas y los casos negativos son las
cargas legitimas.

Consideremos dos escenarios:
 1. si predecimos que la carga es fraudulenta, rechazaremos dicha carga
 2. si predecimos que la carga es fraudulenta, avisaremos cliente para confirmar la carga

En el caso 1, es un gran inconveniente para el ciente cuando el modelo predice un fraude de forma incorrecta
(un falso positivo). En el caso 2, el falso positivo es un menor inconveniente para el cliente.

Cuantos mayor sea el numero de falsos positivos, menor será la precision. Debido al alto coste de los falsos
positivos en el primer caso, valdria la pena tener un recall bajo para tener una precisión muy alta. En el caso
2, se querria un mayor equilibrio entre la precision y el recall.

No hay una regla fija sobre los valores de precisión y recall a los que hay que aspirar. Siempre depende del
conjunto de datos y de la aplicación


    ----------
     F1 SCORE
    ----------

La exactitud (accuracy) era una métrica atractiva porque era solo un número. La precisión y el recall son dos
números, por lo que no siempre es obvio cómo elegir entre dos modelos si uno tiene mayor precisión y el otro
un mayor recall. El F1 Score es una media de la precisión y el recall, de modo que tenemos una única puntuación
para nuestro modelo.

Fórmula matemática del F1 Score:
              precision * recall
    F1 = 2 * --------------------
              precision + recall

De modo que el F1 Score es la media entre la precision y el recall.



