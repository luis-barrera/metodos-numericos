import sys

# Entradas del algoritmo
g = lambda x: (1/2)*(10 - x**3)**(1/2) # Esta es la función g
p0 = 1.5	# Aproximación inicial
TOL = 9.3132e-10	# Tolerancia o epsilon
N = 30	# Número de iteraciones

for i in range(N):
	print("\nIteración", i+1, "#"*10)

	p = g(p0)
	print("Evaluando g({p0}): {p}".format(p0 = p0, p = p))

	dif = p - p0
	print("{p} - {p0} = {dif}".format(p=p, p0=p0, dif=dif))

	if ( dif < 0 ):
		dif = -dif

	if ( dif < TOL ):
		print("{dif} es menor que {TOL}".format(dif = dif, TOL = TOL))
		print("La solución aproximada p es", p)
		sys.exit(0)
	else:
		print("{dif} NO es menor que {TOL}, pasando a la siguiente iteración".format(dif = dif, TOL = TOL))

	p0 = p

print("El método falló después de", N, "iteraciones")
