#Funcion con argumentos variables
def sumador(*args):
    return sum(args)

#Llamar a la funcion
print(sumador(1, 2, 3, 4, 5))
print(sumador(4, 5, 6))