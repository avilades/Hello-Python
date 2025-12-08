set1 = {1, 2}
set2 = {2, 3}

print(set1.union(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.intersection(set2))

print(set1.symmetric_difference(set2))

#discard no da error si no existe el elemento
set1.discard(3)
print(set1)

#remove da error si no existe el elemento
#set1.remove(3)
print(set1)

#pop elimina un elemento aleatorio, no le podemos indicar nuemro porque no tiene orden al ser un set (hash)
set1.pop()
print(set1)

#para verificar si un elemento esta en el set
print(2 in set1)

#clear elimina todos los elementos
set1.clear()
print(set1)

#del elimina el set
del set1
#print(set1)


