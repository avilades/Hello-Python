
'''
lambda es una función de una sola línea diseñada para tareas rápidas y sencillas.

La sintaxis es: lambda argumentos: expresión
'''


# Versión clásica con def
def cuadrado_clasico(x):
    return x ** 2

# Versión Lambda
# Asignamos la lambda a una variable para poder llamarla (aunque esto es raro en la práctica)
cuadrado_lambda = lambda x: x ** 2

print(f"Clásica: {cuadrado_clasico(5)}") # Salida: 25
print(f"Lambda: {cuadrado_lambda(5)}")   # Salida: 25
print(f"Lambda: {(lambda x: x ** 2)(5)}")   # Salida: 25 los argumentos de la lambda van entre parentesis


#Ejemplos de lambda

# Versión clásica con def
def cuadrado_clasico(x):
    return x ** 2

# Versión Lambda
# Asignamos la lambda a una variable para poder llamarla (aunque esto es raro en la práctica)
cuadrado_lambda = lambda x: x ** 2

print(f"Clásica: {cuadrado_clasico(5)}") # Salida: 25
print(f"Lambda: {cuadrado_lambda(5)}")   # Salida: 25




numeros = [1, 2, 3, 4, 5, 6, 7, 8]
# filter(funcion_criterio, lista_datos)
# La lambda recibe cada número 'n' y devuelve True si es par
pares = list(filter(lambda n: n % 2 == 0, numeros))
print(f"Filtramos los números pares: {pares}")
# Salida: [2, 4, 6, 8]



#hacemos un map para aplicar la lambda a cada número y el list para convertirlo en una lista
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"Aplicamos la lambda a cada número: {list(cuadrados)}")

estudiantes = [("Ana", 25), ("Pedro", 19), ("Luis", 30)]
# sorted(lista, key=funcion_que_dice_por_que_ordenar)
# La lambda recibe la tupla 'x' (ej: ("Ana", 25)) y devuelve x[1] (la edad)
estudiantes_ordenados = sorted(estudiantes, key=lambda x: x[1])

print(estudiantes_ordenados)
# Salida: [('Pedro', 19), ('Ana', 25), ('Luis', 30)]




# Ejemplo de lambda con map
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
# map(funcion, lista_datos)
# La lambda recibe cada número 'n' y devuelve n * 2
numeros_duplicados = list(map(lambda n: n * 2, numeros))

print(numeros_duplicados)
# Salida: [2, 4, 6, 8, 10, 12, 14, 16]




'''
4 Ejercicios
Intenta resolverlos tú mismo antes de mirar las soluciones. ¡Ánimo!
Conversor rápido: Crea una función lambda que convierta grados Celsius a Fahrenheit. La fórmula es: $F = (C \times 1.8) + 32$. Pruébala con 30 grados.
Filtrar palabras: Tienes la lista palabras = ["sol", "montaña", "luz", "cielo", "mar"]. Usa filter y una lambda para obtener solo las palabras que tengan menos de 4 letras.
Transformar lista: Tienes la lista precios = [100, 200, 50, 40]. Usa map y una lambda para obtener una nueva lista con los precios con un 10% de descuento aplicado (multiplicar por 0.9).
Ordenar diccionarios: Tienes una lista de diccionarios:usuarios = [{"nombre": "Juan", "id": 3}, {"nombre": "Sara", "id": 1}, {"nombre": "Marta", "id": 2}].Usa sorted y una lambda para ordenarlos por su "id".
'''

print(f"\nEmpezamos con los ejercicios de lambda\n")

conversor = lambda c: (c * 1.8) + 32
print(f"Convertimos 30 grados Celsius a Fahrenheit: {(lambda c: (c * 1.8) + 32) (30)}")
print(conversor(30))




palabras = ["sol", "montaña", "luz", "cielo", "mar"]
print(f"Filtramos las palabras con menos de 4 letras: {list(filter(lambda palabra: len(palabra) < 4, palabras))}")

print(f"Filtramos las palabras con menos de 4 letras: {list(filter(lambda palabra: len(palabra) < 4, ["sol", "montaña", "luz", "cielo", "mar"]))}")



precios = [100, 200, 50, 40]
print(f"Aplicamos un descuento del 10% a los precios: {list(map(lambda precio: precio * 0.9, precios))}")


usuarios = [{"nombre": "Juan", "id": 3}, {"nombre": "Sara", "id": 1}, {"nombre": "Marta", "id": 2}]
print(f"Ordenamos los usuarios por su id: {sorted(usuarios, key=lambda u: u['id'])}")


'''














palabras = ["sol", "montaña", "luz", "cielo", "mar"]
palabras_filtradas = list(filter(lambda p: len(p) < 4, palabras))
print(palabras_filtradas)

precios = [100, 200, 50, 40]
precios_descuento = list(map(lambda p: p * 0.9, precios))
print(precios_descuento)

usuarios = [{"nombre": "Juan", "id": 3}, {"nombre": "Sara", "id": 1}, {"nombre": "Marta", "id": 2}]
usuarios_ordenados = sorted(usuarios, key=lambda u: u["id"])
print(usuarios_ordenados)


'''