# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=10172

### Higher Order Functions ###

# Funciones de Orden Superior: Son funciones que pueden recibir otras funciones
# como argumentos o devolver funciones como resultado.

from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


# Esta función recibe otra función 'f_sum' como argumento y la usa
def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

### Closures ###

# Un Closure es una función que recuerda variables de su entorno superior
# incluso después de que ese entorno haya terminado su ejecución.

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add


add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))

### Built-in Higher Order Functions ###
# Python tiene funciones de orden superior muy útiles ya integradas

numbers = [2, 5, 10, 21, 3, 30]

# Map
# Aplica una función a cada elemento de una lista (iterable)

def multiply_two(number):
    return number * 2


print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter
# Filtra los elementos de una lista basándose en si una función devuelve True

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
# Aplica una función de forma acumulativa a los elementos de una lista, reduciéndola a un solo valor.

def sum_two_values(first_value, second_value):
    return first_value + second_value


print(reduce(sum_two_values, numbers))

