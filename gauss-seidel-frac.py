# TODO: verificar que sea una matriz diagonalmente dominante
# TODO: en caso de que NO sea diagonalmente dominante hacer el intercambio de renglones
# TODO: quitar el signo + de el ultimo renglón de cada iteración
# TODO: permitir que se introduzca los parámetros y la matriz desde la terminal

import numpy as np
from fractions import Fraction as frac


def suma_renglones(i, n, A, x):
    suma = 0

    for j in range(n):
        if j != i:
            suma += A[i][j] * x[j]
            print("(", frac(A[i][j]), "*", frac(x[j]), ")", sep="", end="")
        if (j != i and j < n-1):
            print("+", end="")

    print(" =", frac(suma))
    return suma


A = [['6', '-3', '2'], ['-1', '4', '1'], ['1', '3', '6']]
b = ['-4', '8', '-15']
x = ['0', '0', '0']

for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j] = frac(A[i][j])

for j in range(len(b)):
    b[j] = frac(b[j])

for j in range(len(b)):
    x[j] = frac(x[j])

n = len(A[0])
itmax = 3    # número de iteraciones
tol = 0.8    # Tolerancia
k = 1


# Iteración de Gauss-Seidel
for k in range(itmax):

    print("Iteracion", k+1)

    for i in range(n):
        suma = suma_renglones(i, n, A, x)
        x[i] = (b[i] - suma) / A[i][i]
        print("x[{index}] = (({b})-({sum})) / {a} = {x}".format(index=i+1, b=b[i], sum=frac(suma), a=frac(A[i][i]), x=frac(x[i])), sep="")
        print()

    print("x{k}:".format(k=k+1), end='')
    B = np.copy(x)
    for j in range(len(x)):
        B[j] = str(x[j])
    print(B)

    print("\n" + "#"*30)
