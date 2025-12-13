# 1. Genera una lista utilizando comprensión con los números del 0 al 10.

numbers = [i for i in range(11)]
print(numbers)

# 2. Crea una lista utilizando comprensión con los cuadrados de los números del 1 al 10.

squares = [i**2 for i in range(1, 11)]
print(squares)

# 3. Genera una lista utilizando comprensión con los números pares del 0 al 20.

even = [i for i in range(21) if i % 2 == 0]
print(even)

# 4. Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprensión.

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)

# 5. Crea una lista utilizando comprensión con los caracteres de una cadena.

text = "Python"
characters = [character for character in text]
print(characters)

# 6. Filtra una lista de palabras y deja solo las que tienen más de 4 letras utilizando comprensión.

words = ["brais", "moure", "dev", "hola", "python"]
large = [p for p in words if len(p) > 4]
print(large)

# 7. Aumenta en 5 cada número de una lista con comprensión usando una función externa.


def sum_five(n):
    return n + 5


numbers = [1, 2, 3, 4, 5]
result = [sum_five(n) for n in numbers]
print(result)

# 8. Crea una lista de booleanos que indique si cada número es mayor que 10 utilizando comprensión.

numbers = [2, 15, 9, 42, 3]
greater = [n > 10 for n in numbers]
print(greater)

# 9. Multiplica solo los números impares por 3 en una lista utilizando comprensión.

numbers = [1, 2, 3, 4, 5, 6]
odds_divisible_by_3 = [n * 3 for n in numbers if n % 2 != 0]
print(odds_divisible_by_3)

# 10. Usa comprensión de listas anidada para generar una matriz 3x3 con números del 1 al 9.

matrix = [[row * 3 + col + 1 for col in range(3)] for row in range(3)]
print(matrix)