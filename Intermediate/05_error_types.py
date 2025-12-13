# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=12721

### Error Types ###

# Capturar y entender los errores es fundamental en programación.
# Aquí vemos los tipos más comunes de errores (Excepciones) en Python.

# SyntaxError
# Ocurre cuando el código no sigue las reglas gramaticales de Python.
# print "¡Hola comunidad!" # Descomentar para Error (Faltan paréntesis)
from math import pi
import math
print("¡Hola comunidad!")

# NameError
# Ocurre cuando intentamos usar una variable que no ha sido definida.
language = "Spanish"  # Comentar para Error
print(language)

# IndexError
# Ocurre cuando intentamos acceder a una posición que no existe en una lista.
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # Descomentar para Error (La lista solo tiene índices 0-4)

# ModuleNotFoundError
# Ocurre cuando intentamos importar un módulo o librería que no existe o no está instalado.
# import maths # Descomentar para Error (El módulo se llama 'math', no 'maths')

# AttributeError
# Ocurre cuando intentamos acceder a un atributo o función que no existe en el objeto.
# print(math.PI) # Descomentar para Error (En math es .pi minúscula, no .PI)
print(math.pi)

# KeyError
# Ocurre cuando intentamos acceder a una clave que no existe en un diccionario.
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error (Error tipográfico en la clave)
print(my_dict["Apellido"])

# TypeError
# Ocurre cuando realizamos una operación con un tipo de dato incorrecto (ej. sumar texto con número, o usar texto como índice de lista).
# print(my_list["0"]) # Descomentar para Error (Los índices de lista deben ser enteros)
print(my_list[0])
print(my_list[False]) # False equivale a 0 en Python, por eso funciona

# ImportError
# Ocurre cuando el módulo existe, pero lo que intentamos importar de él no.
# from math import PI # Descomentar para Error
print(pi)

# ValueError
# Ocurre cuando una función recibe un argumento del tipo correcto pero con un valor inapropiado.
# my_int = int("10 Años") # Descomentar para Error (No puede convertir "10 Años" a número)
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
# Ocurre matématicamente al intentar dividir por cero.
# print(4/0) # Descomentar para Error
print(4/2)
