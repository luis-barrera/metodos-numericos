import sys

# Entradas para el algoritmo
# f = lambda x: x**2 + x/4 + 19
f = lambda x: (1/2)*(10 - x**3)**(1/2) # La función
a, b = 1, 2    # Los endpoints
# TOL = 0.05    # Tolerancia o epsilon
TOL = 9.3132e-10    # Tolerancia o epsilon
N = 30    # Número de interaciones


# Digitos de redondeo
digs = 4
rd = lambda a: round(a, digs)

# Verificamos que f(a) y f(b) sean de signos contrarios

FA = rd(f(a))


for i in range(N):
    print("\nIteración", i+1, "#"*10)

    p = rd(a + (b - a)/2)
    print("p = {a} + ({b} - {a})/2 = {p}".format(p=p, a=a, b=b))
    FP = rd(f(p))
    print("Evaluando f({p}): {FP}".format(p = p, FP=FP))

    if (( FP == 0 ) or ( (b - a)/2 < TOL )):
        if ( FP == 0 ):
            print("FP = 0")
        if ( (b - a)/2 < TOL ):
            print("(b - a)/2 < TOL")
        print('\033[93m' + "La solución aproximada p es", p)
        sys.exit(0)

    if ( (FA*FP) > 0 ):
        print("Reasignando a <- p")
        a = p

        print("Reasignando FA <- FP")
        FA = FP
    else:
        print("Reasignando b <- p")
        b = p

print("El método falló después de", N, "iteraciones")
