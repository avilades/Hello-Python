# 1. Crea un módulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos números. Importa este módulo en otro archivo y usa sus funciones.

# calculator.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    return a / b

# Importación desde otro fichero

# from calculator import add, subtract, multiply, divide
# print(add(5, 3))
# print(subtract(5, 3))
# print(multiply(5, 3))
# print(divide(5, 3))


# 2. Crea un módulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este módulo y realice conversiones.

# converter.py

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Importación desde otro fichero

# from converter import celsius_to_fahrenheit, fahrenheit_to_celsius
# print(celsius_to_fahrenheit(25))
# print(fahrenheit_to_celsius(77))


# 3. Crea un módulo que contenga una lista de nombres de estudiantes y una función que imprima todos los nombres. Importa este módulo en otro archivo y usa la función para mostrar la lista.

# students.py

students_list = ["Alice", "Bob", "Charlie", "Diana"]


def print_students():
    for student in students_list:
        print(student)

# Importación desde otro fichero

# from students import print_students
# print_students()


# 4. Crea un módulo llamado "geometry" que tenga una función para calcular el área de un círculo y un cuadrado. Usa este módulo en otro archivo para calcular áreas.

# geometry.py

def area_circle(radius):
    return 3.14159 * radius ** 2


def area_square(side):
    return side * side

# Importación desde otro fichero

# from geometry import area_circle, area_square
# print(area_circle(5))
# print(area_square(4))


# 5. Escribe un módulo que contenga una función que acepte cualquier número de argumentos y devuelva su suma. Importa y usa la función en otro archivo.

# sum_module.py

def sum_all(*args):
    return sum(args)

# Importación desde otro fichero

# from sum_module import sum_all
# print(sum_all(1, 2, 3, 4))


# 6. Crea un módulo que defina una clase llamada "Car" con propiedades como marca, modelo y año. Importa este módulo en otro archivo y crea una instancia de la clase "Car".

# car_module.py

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.brand} {self.model}, {self.year}"

# Importación desde otro fichero

# from car_module import Car
# my_car = Car("Toyota", "Corolla", 2020)
# print(my_car.display_info())


# 7. Escribe un módulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.

# file_module.py

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Importación desde otro fichero

# from file_module import write_to_file, read_from_file
# write_to_file("example.txt", "Hola, Python")
# print(read_from_file("example.txt"))


# 8. Crea un módulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de números. Usa este módulo para calcular estos valores en una lista dada.

# statistics.py

def mean(numbers):
    return sum(numbers) / len(numbers)


def median(numbers):
    sorted_numbers = sorted(numbers)
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

# Importación desde otro fichero

# from statistics import mean, median
# numbers = [1, 2, 3, 4, 5]
# print(mean(numbers))
# print(median(numbers))


# 9. Crea un módulo que contenga una función para contar cuántas veces aparece una palabra en un texto. Escribe un programa que importe el módulo y lo use para contar palabras en una cadena.

# word_count.py

def count_word(text, word):
    return text.lower().split().count(word.lower())

# Importación desde otro fichero

# from word_count import count_word
# text = "Python is great and Python is fun"
# print(count_word(text, "python"))


# 10 Crea un módulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este módulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas específicas.

# dates.py

from datetime import datetime  # Módulo nativo de Python

def get_current_date():
    return datetime.now().strftime("%d-%m-%Y")


def date_difference(date1, date2):
    d1 = datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.strptime(date2, "%d-%m-%Y")
    return abs((d2 - d1).days)

# Importación desde otro fichero

# from dates import get_current_date, date_difference
# print(get_current_date())
# print(date_difference("2024-01-01", "2024-10-01"))