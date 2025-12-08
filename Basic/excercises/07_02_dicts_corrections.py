# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.

my_dict = {"name": "Brais", "age": 25, "country": "Galicia"}
print(my_dict)

# 2. Accede al valor de la clave name en el diccionario.

print(my_dict["name"])

# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.

my_dict["job"] = "Programador"
print(my_dict)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.

my_dict["age"] = 38
print(my_dict)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.

del my_dict["country"]
print(my_dict)

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).

squares = {x: x**2 for x in range(1, 6)}
print(squares)

# 7. Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.

print("age" in my_dict)

# 8. Imprime solo las claves del diccionario.

print(my_dict.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.

print(list(my_dict.keys()))

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".

my_keys = ["name", "age", "job"]
my_new_dict = dict.fromkeys(my_keys, "Desconocido")
print(my_new_dict)

print(my_new_dict.values())
print(f"Imprimimos  my_new_dict.items(): {my_new_dict.items()}")
#devuleve KeyError por que  no existe la clave
#print(my_new_dict["nonexisting_key"])