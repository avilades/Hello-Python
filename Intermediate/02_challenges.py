# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=4142

### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def fizzbuzz():
    # Iteramos desde 1 hasta 100 (101 no está incluido)
    for index in range(1, 101):
        # Primero comprobamos la condición más específica: múltiplo de 3 Y 5 (múltiplo de 15)
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        # Si no, comprobamos si es múltiplo de 3
        elif index % 3 == 0:
            print("fizz")
        # Si no, comprobamos si es múltiplo de 5
        elif index % 5 == 0:
            print("buzz")
        # Si no es ninguno de los anteriores, imprimimos el número
        else:
            print(index)


fizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""


def is_anagram(word_one, word_two):
    # Si son exactamente iguales, no cuentan como anagrama según el enunciado
    if word_one.lower() == word_two.lower():
        return False
    # Ordenamos las letras de ambas palabras y las comparamos.
    # Si tienen las mismas letras ordenadas, son anagramas.
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("Amor", "Roma"))

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""


def fibonacci():

    prev = 0
    next = 1

    for index in range(0, 50):
        print(prev) # Imprimimos el número actual de la serie
        # Calculamos el siguiente número sumando los dos anteriores
        fib = prev + next
        # Actualizamos los valores para la siguiente iteración
        prev = next
        next = fib


fibonacci()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""


def is_prime():

    for number in range(1, 101):

        # Los números primos deben ser mayor o igual a 2
        if number >= 2:

            is_divisible = False

            # Comprobamos si es divisible por algún número entre 2 y él mismo (no incluido)
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break # Si encontramos un divisor, ya sabemos que no es primo, salimos del bucle.

            # Si no encontramos ningún divisor, es primo.
            if not is_divisible:
                print(number)


is_prime()

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""


def reverse(text):
    text_len = len(text)
    reversed_text = ""
    # Recorremos la longitud del texto
    for index in range(0, text_len):
        # Vamos construyendo la nueva cadena tomando caracteres desde el final hacia el principio
        reversed_text += text[text_len - index - 1]
    return reversed_text


print(reverse("Hola mundo"))

