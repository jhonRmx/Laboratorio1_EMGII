# Diccionario -> almacen a pares de cave-valor
mi_diccionario = {'nombre': 'Jhonatan Laruta', 'edad': 20, 'ciudad': 'El Alto'}
print(mi_diccionario)

# Acceder a un valor
print(mi_diccionario['nombre'])
print(mi_diccionario['ciudad'])

# Agregar elementos
mi_diccionario['profesion'] = 'Ingeniero'
print(mi_diccionario)

# Eliminar elementos
del mi_diccionario['ciudad']
print(mi_diccionario)

#Obtener claves del diccionario
print(mi_diccionario.keys())

#Obtener valores del diccionario
print(mi_diccionario.values())  

#Verificar si una clave existe
if 'ciudad' in mi_diccionario:
    print("Clave encontrada")

#Recorrido de un diccionario
for clave, valor in mi_diccionario.items():
    print("[Clave:]", clave, "[Valor:]", valor)