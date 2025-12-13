# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=3239

### List Comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

# Definición

# Una "List Comprehension" (compresión de lista) permite crear una lista
# a partir de otra de forma concisa y rápida en una sola línea.
# Sintaxis: [expresión for elemento in iterable]

# Ejemplo básico: Crear lista copiando valores de un rango
my_list = [i for i in range(8)]
print(my_list)

# Ejemplo con operación: Sumar 1 a cada elemento
my_list = [i + 1 for i in range(8)]
print(my_list)

# Ejemplo con operación: Multiplicar por 2 cada elemento
my_list = [i * 2 for i in range(8)]
print(my_list)

# Ejemplo con operación: Elevar al cuadrado
my_list = [i * i for i in range(8)]
print(my_list)


def sum_five(number):
    return number + 5


# Podemos usar funciones dentro de la comprensión de listas
my_list = [sum_five(i) for i in range(8)]
print(my_list)

