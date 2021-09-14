# TODO: Darle formato a la salida

def suma_renglon(i):
	suma = 0

	for j in range(i + 1, n):
		suma += A[i][j] * x[j]

	return suma


# Matriz aumentada
A = [[6, -3, 2, -4], [-1, 4, 1, 8], [1, 3, 6, -15]]
# A = [[0, -3, 2, -4], [0, 4, 1, 8], [0, 3, 6, -15]]

# Tamaño de la matriz, renglones
n = len(A)

x = [0] * n
m = [0] * n


# Algoritmo de sustitución Gaussiana con sustitución hacia atrás
for i in range(n - 1):
	# Suponemos que todos los números de la columna son 0
	diferente_a_cero = False

	for p in range(i, n):
		# Vamos a recorrer todos los elementos de una columna, si no
		# encontramos un número diferente a 0 terminamos el programa
		if ( A[p][i] != 0 ):
			diferente_a_cero = True	# Si hay un número que es diferente a cero
			break

	if ( not diferente_a_cero ):
		print("No unique solution exists")
		quit()

	if ( p != i ):
		aux = A[p]
		A[p] = A[i]
		A[i] = aux

	for j in range(i + 1, n):
		m[j] = A[j][i] / A[i][i]

		for k in range(n + 1):
			A[j][k] = A[j][k] - ( m[j] * A[i][k] )


if ( A[n-1][n-1] == 0 ):
	print("No unique solution exists")
	quit()


# Empieza la sistitución hacia atrás
x[n-1] = A[n-1][n] / A[n-1][n-1]


for i in range(n - 1, -1, -1):
	x[i] = ( A[i][n] - suma_renglon(i) ) / A[i][i]


print(x)
