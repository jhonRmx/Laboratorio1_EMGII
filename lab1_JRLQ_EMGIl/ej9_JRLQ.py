# Metodos de listas
numeros = [1, 2, 3, 4, 5]

#Adicionar elementos 
numeros.append(6)
print(numeros)

#{insertar elementos en una posision determinada
numeros.insert(0, -1)
print(numeros)

numeros.insert(1,0)
print(numeros)

#Eliminar un elemento
numeros.remove(1)
print(numeros)

#Verificar si un elemento se encuentra en la lista
print(4 in numeros)

#Tamaño de la lista
print(len(numeros))

#Eliminar el contenido de la lista
numeros.clear()
print(numeros)