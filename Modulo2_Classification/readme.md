En el machine learning de alto nivel tenemos el aprendizaje supervisado o no supervisado
El aprendizaje supervisado implica que hay datos historicos previos, en el no supervisado, no.

En el aprendizaje supervisado hay dos tipos de problemas:
 - clasificacion (Verdadero o Falso, a veces hay otras categorias)
 - regresion (valores numericos)

target - el objetivo a predecir
feature - las caracteristicas que podemos usar para hacer la prediccion

En un problema de clasificaion, construiremos un modelo para separar los
casos positivos de los negativos y que prediga futuros casos.

--------------------------------
MODELO LINEAL PARA CLASIFICACION
--------------------------------

La linea viene definida por la ecuacion: 0 = ax + by + c
Si los valores (x,y) que le proporcionemos a la recta caen a la derecha
se cumplira una categoria, pero si caen a la izquierda se cumplira lo opuesto.

Lo que hace buena a la linea es que sea capaz de separar lo mejor posible
a las dos clases que queremos clasificar

#PROBABILIDAD
Podemos evaluar la probabilidad de que un dato pertenezca a una categoria. Para
ello veriamos lo evaluamos entre 0 y 1. Si es 0.5 no podemos determinar el resultado.
cuanto mas cerca este de 1 mas probabilidad hay de que cumpla y viceversa.

La formula para determinar esto es: 1 / (1 + e^(-ax+by+c))

La regresion logistica proporciona no solo una prediccion (categoria 1 o 2), sino
que proporciona una probabilidad (80% de categoria 1)


#LA MEJOR LINEA
Para calcular como de buena es nuestra linea tenemos que evaluar si nuestras
predicciones son correctas.

Ecuacion Likelihood
             { p  si el dato cumple la condicion
Likelihood = {
             { 1 - p  si el dato no cumple la condicion

Si predecimos que p es 0.25 y el dato no cumple la condicion, tendremos
una puntuacion de 0.75(bueno)
Si predecimos que p es 0.25 y el dato cumple la condicion, tenedremos
una puntuacion de 0.25(malo)

Tendremos que multiplicar todas las puntuaciones obtenidas para saber si
nuestra linea es buena o no. Asi podremos evaluar diferentes lineas y buscar
la mejor.
El valor de la multiplicacion siempre tenderá a ser muy pequeño, ya que es la
probabilidad de que este modelo prediga de una forma perfecta
