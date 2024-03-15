# Ultima-evaluacion-KKT
Algoritmo de Karush Kuhn Tucker
Tenemos una representación de como sería un algoritmos del teorema de KKT

En el código tenemos una librería de python llamado sympy, la cual importa funciones que facilitan la resolución de problemas matemáticos como en el caso de KKT

Primero estan las variables simbólicas. Se simbolizan estas variables (x, y, l1 y l2) para que la librería la pueda utilizar, dese cuenta que symbols y solve están siendo importadas de la librería sympy.
Las variables simbólicas son las variables a utilizar en este caso es X y Y, si se fija en tanto en las inecuaciones, ecuaciones y la función optimizar aparece esas variables, y L1 y L2 son necesarios para calcular las ecuaciones y las funciones de Lagrange, que son los derivados 

Teniendo en cuenta ya las variables que vamos a utilizar Esta es la función que estamos utilizando 0.16 . x al cuadrado + 0.2x . y + 0.09y².

Abajo están las restricciones x + y. El 1 lo pasamos restando y el 0.09 lo pasamos para el otro lado restando tambien, teniendo aquí las dos restricciones 

Con la librería de matemáticas anteriormente mencionada podemos sacar la matriz hessiana, el gradiante que es jacobiano, utilizamos las fórmulas (ecuaciones de kkt), derivamos en cada punto la función, se resuelve el sistema de ecuaciones y evaluamos la solución en la función objetivo qué es simplemente la sustitución de los puntos en la función para así comprobarlo.

Y al final se imprimen los valores
