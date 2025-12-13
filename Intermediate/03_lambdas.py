# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=9145

### Lambdas ###

# Las funciones lambda son funciones anónimas, es decir, sin nombre.
# Se definen en una sola línea y son útiles para operaciones cortas.
# Sintaxis: lambda argumentos: expresión

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))

# Lambda con operaciones más "complejas"
multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

# Lambdas dentro de funciones: Útil para crear funciones que generan otras funciones
def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

# Aquí creamos una función que espera 2 valores, y 'value' ya está predefinido como 5
print(sum_three_values(5)(2, 4))
