#Sentencias
temperatura = int(input("Ingrese la temperatura actual: "))

if temperatura > 28:
    print("Esta haciendo calor")
else:
    print("Hace frio")

if temperatura > 28:
    print("Esta haciendo calor")
elif temperatura > 20:
    print("Es un dia agradable")
elif temperatura > 10:
    print("Hace un poco de frio")
else:
    print("Hace frio, brrr")

print("Proceso concluido")