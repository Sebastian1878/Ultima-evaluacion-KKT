#Algoritmo de Karush Kuhn Tucker
import sympy as sp
from sympy import symbols, solve

#variables simbolicas
x, y, l1, l2 = symbols('x y l1 l2')

#funcion objetivo
f = 0.16*x**2 + 0.2*x*y + 0.09*y**2

#restricciones
g1 = x + y - 1
g2 = 0.11*x+0.08*y - 0.09

#Obtener la matriz Hessiana
hess = sp.hessian(f, (x, y))

#Obtener el gradiente
grad = sp.Matrix([f]).jacobian([x, y])

#ecuaciones de KKT
kkt = f - l1*g1 - l2*g2

#Derivamos la funcion de Lagrange
dLx1 = sp.diff(kkt, x)
dLx2 = sp.diff(kkt, y)
dLl1 = sp.diff(kkt, l1)
dLl2 = sp.diff(kkt, l2)

#Resolvemos el sistema de ecuaciones
sol = solve([dLx1, dLx2, dLl1, dLl2], (x, y, l1, l2))

#Evaluamos la solucion en la funcion objetivo
valorOptimo = f.subs(sol)

#Imprimimos la solucion
print("El par ordenado es: [", sol.get(x), ",", sol.get(y), "]" )
print("El valor optimo es: ", valorOptimo)
print("La matriz Hessiana es: ", hess)
print("El gradiente es: ", grad)