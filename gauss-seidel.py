# TODO: verificar que sea una matriz diagonalmente dominante
# TODO: en caso de que NO sea diagonalmente dominante hacer el intercambio de renglones
# TODO: quitar el signo + de el ultimo renglón de cada iteración
# TODO: permitir que se introduzca los parámetros y la matriz desde la terminal

A = [[6, -3, 2], [-1, 4, 1], [1, 3, 6]]
b = [-4, 8, -15]
x = [0, 0, 0]

n = len(A[0])
itmax = 3	# número de iteraciones


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


# Iteración de Gauss-Seidel
for k in range(itmax):

	print("Iteracion", k+1)

	for i in range(n):
		suma = suma_renglones(i, n, A, x)
		x[i] = round((b[i] - suma) / A[i][i], 4)
		print("x[{index}] = (({b})-({sum})) / {a} = {x}".format(index=i+1, b=b[i], sum=suma, a=A[i][i], x=x[i]), sep="")
		print()

	print("x{k}:".format(k=k+1), x)
	print("#"*30)