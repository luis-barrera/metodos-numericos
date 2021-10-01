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
            print("(", A[i][j], "*", x[j], ")", sep="", end="")
        if (j != i and j < n-1):
            print("+", end="")

    print(" =", suma)
    return suma


A = [['6', '-3', '2'], ['-1', '4', '1'], ['1', '3', '6']]
b = ['-4', '8', '-15']
x = ['0', '0', '0']

n = len(A[0])
itmax = 3

u = ['0'] * n


for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j] = frac(A[i][j])

for i in range(len(x)):
    b[i] = frac(b[i])

for i in range(len(x)):
    x[i] = frac(x[i])


# Iteración de Jacobi
#   itmax es el número de iteraciones
for k in range(itmax):

    print("Iteracion", k+1)

    for i in range(n):
        suma = suma_renglones(i, n, A, x)
        u[i] = round((b[i] - suma) / A[i][i], 4)
        print("u[{index}] = (({b})-({sum})) / {a} = {u}".format(index=i, b=b[i], sum=suma, a=A[i][i], u=u[i]), sep="")
        print()

    for i in range(n):
        x[i] = u[i]

    print("x{k}:".format(k=k+1), end='')
    B = np.copy(x)
    for j in range(len(x)):
        B[j] = str(x[j])
    print(B)

    print("\n" + "#"*30)
