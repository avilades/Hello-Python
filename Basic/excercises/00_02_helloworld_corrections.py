# 1. Imprime "¡Hola Mundo!" por consola.

print("¡Hola Mundo!")

# 2. Escribe un comentario de una sola línea explicando qué hace el código del Ejercicio 1.

# Este código imprime "¡Hola Mundo!" por consola.

# 3. Imprime tu nombre y edad en la misma línea utilizando la función print.

print("Mi nombre es Alvaro y tengo", 45, "años.")

# 4. Usa la función type() para imprimir el tipo de dato de una cadena de texto, un número entero y un número decimal.

print(type("Alvaro"))  # str
print(type(45))       # int
print(type(3.14))     # float

# 5. Escribe un comentario en varias líneas explicando qué son los tipos de datos en Python.

"""
En Python, los tipos de datos más comunes son:
- str: para cadenas de texto
- int: para números enteros
- float: para números con decimales
- bool: para valores booleanos (True/False)
"""

# 6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".

print("Hola" + " " + "Mundo")

# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma línea.

my_name = "Alvaro"
my_age = 45
print("Mi nombre es", my_name, "y tengo", my_age, "años.")

# 8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.

user_name = input("¿Cuál es tu nombre? ")
print("¡Hola", user_name + "!")

# 9. Usa print() para mostrar el resultado de la suma de dos números enteros y el tipo de dato resultante.

result = 5 + 10
print("El resultado es:", result)
print("El tipo de dato del resultado es:", type(result))

# 10. Comenta el código del Ejercicio 9, y explica qué hace cada línea usando comentarios de una sola línea.

# Suma dos números enteros.
result = 5 + 10

# Imprime el resultado de la suma.
print("El resultado es:", result)

# Imprime el tipo de dato del resultado, que es 'int'.
print("El tipo de dato del resultado es:", type(result))