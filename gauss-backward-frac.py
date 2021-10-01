import numpy as np
from fractions import Fraction as frac


def imprimir_matriz(A):
    B = np.copy(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[i][j] = str(A[i][j])
    print(np.matrix(B))

def suma_renglon(i):
    suma = 0

    if (i != n - 1):
        print("\nSumando el {renglon} renglón".format(renglon = i + 1))
    else:
        return 0

    for j in range(i + 1, n):
        suma += A[i][j] * x[j]
        print("(", frac(A[i][j]), "*", frac(x[j]), ")", sep="", end="")
        if (j < n - 1):
            print("+", end="")

    print(" =", frac(suma))
    return suma


# Matriz aumentada
# A = [[6, -3, 2, -4], [-1, 4, 1, 8], [1, 3, 6, -15]]
# A = [[0, -3, 2, -4], [0, 4, 1, 8], [0, 3, 6, -15]]
# A = [[1,1,1/2],[-3,-6,-5]]
A = [['-1/3','1','35/18'],['-61/6','-8/3','-17/3']]

for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j] = frac(A[i][j])

# Tamaño de la matriz, renglones
n = len(A)

x = ['0'] * n
m = ['0'] * n


print("Matriz A:")
imprimir_matriz(A)
print("")

# Algoritmo de sustitución Gaussiana con sustitución hacia atrás
for i in range(n - 1):
    # Suponemos que todos los números de la columna son 0
    diferente_a_cero = False

    for p in range(i, n):
        # Vamos a recorrer todos los elementos de una columna, si no
        # encontramos un número diferente a 0 terminamos el programa
        if ( A[p][i] != frac(0) ):
            diferente_a_cero = True    # Sí hay un número que es diferente a cero
            break

    if ( not diferente_a_cero ):
        print("No unique solution exists")
        quit()

    if ( p != i ):
        print("Intercambiando renglón {ren1} por {ren2}".format(ren1=p, ren2=i))
        aux = A[p]
        A[p] = A[i]
        A[i] = aux

        print("Matriz A:")
        print(np.matrix(A))
        print("")

    for j in range(i + 1, n):
        m[j] = A[j][i] / A[i][i]

        print("\nEl valor de m[{j_aux}] = {Aji} / {Aii} = {mj}"
            .format(j_aux = j, mj = frac(m[j]), Aji = frac(A[j][i]), Aii = frac(A[i][i])))

        for k in range(n + 1):
            valor_anterior = A[j][k]
            A[j][k] = valor_anterior - ( m[j] * A[i][k] )

            print("\nEl valor de A[{j}][{k}] es : A[{j}][{k}] - (m[{j}] * A[{i}][{k}])"
                .format(i = i, j = j, k = k, mj = frac(m[j])))
            print("\nEl valor de A[{j}][{k}] es : {anterior} - ({mj} * {Aik}) = {Ajk}"
                .format(i = i, j = j, k = k, anterior = frac(valor_anterior), mj = frac(m[j]), Aik = frac(A[i][k]), Ajk = frac(A[j][k])))

print("")
print("Matriz A después del intercambio de renglones:")
imprimir_matriz(A)


if ( A[n-1][n-1] == 0 ):
    print("No unique solution exists")
    quit()


print("\n\n", "#"*30, sep="")
print("Inicia la sustitución hacia atrás")

# Empieza la sistitución hacia atrás
x[n-1] = A[n-1][n] / A[n-1][n-1]

print("A[{a1}][{a2}] / A[{a1}][{a1}] = x[{a1}]"
    .format(a1 = n, a2 = n+1))
print("{b} / {an} = {xn}"
    .format(xn = frac(x[n - 1]), b = frac(A[n-1][n]), an = frac(A[n-1][n-1])))


for i in range(n - 1, -1, -1):
    suma = suma_renglon(i)
    print("\n")

    x[i] = ( A[i][n] - suma ) / A[i][i]

    print("x[{a1}] = (A[{a1}][{a2}] - (Sumatoria del renglón desde A[{a1}][{a3}] * x[{a3}])) / A[{a1}][{a1}]"
        .format(a1 = i + 1, a2 = n+1, a3 = i + 2))

    print("( {b} - {suma} ) / {Aii} = {xn}"
        .format(xn = frac(x[i]), b = frac(A[i][n]), Aii = frac(A[i][i]), suma = suma))


print("\nSolución x:")
B = np.copy(x)
for j in range(len(x)):
    B[j] = str(x[j])
print(B)
