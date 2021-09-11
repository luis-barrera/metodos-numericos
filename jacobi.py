# TODO: verificar que sea una matriz diagonalmente dominante
# TODO: en caso de que NO sea diagonalmente dominante hacer el intercambio de renglones

A = [[6, -3, 2], [-1, 4, 1], [1, 3, 6]]
b = [-4, 8, -15]
x = [0, 0, 0]

u = [0, 0, 0]
n = len(A[0])
itmax = 3


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


# Iteración de Jacobi
#   itmax := número de iteraciones
for k in range(itmax):

	print("Iteracion", k+1)

	for i in range(n):
		suma = suma_renglones(i, n, A, x)
		u[i] = round((b[i] - suma) / A[i][i], 4)
		print("u[{index}] = (({b})-({sum})) / {a} = {u}".format(index=i, b=b[i], sum=suma, a=A[i][i], u=u[i]), sep="")
		print()

	for i in range(n):
		x[i] = u[i]

	print("x:", x)
	print("#"*30)
