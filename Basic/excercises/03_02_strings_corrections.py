# 1. Declara una variable text con la frase "Aprendiendo Python" y luego imprime la longitud de la cadena usando len().

text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: "Hola" y "Python", y muestra el resultado en una sola línea.

print("Hola" + " " + "Mundo pythonico")

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.

text = "Esta es una línea\nEsta es otra línea"
print(text)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.

name = "Alvaro"
surname = "Tester"
age = 45
print(f"Mi nombre es {name} {surname} y tengo {age} años")

# 5. Desempaqueta los caracteres de la palabra "Python" en variables separadas y luego imprímelos uno por uno.

palabra = "Python"
a, b, c, d, e, f = palabra
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un "slice" de la palabra "Programación" para obtener los caracteres desde la posición 3 hasta la 7.

text = "Programación"
text_slice = text[3:7]
print(text_slice)

# 7. Invierte la cadena "Python" usando slicing y muestra el resultado.

text = "Python"
reversed_text = text[::-1]
print(reversed_text)

# 8. Convierte la cadena "aprendiendo python" en mayúsculas usando el método adecuado e imprímela.

text = "aprendiendo python"
print(text.upper())

# 9. Cuenta cuántas veces aparece la letra "n" en la cadena "Programación en Python".

text = "Programación en Python"
print(text.count("n"))

# 10. Verifica si la cadena "12345" es numérica usando el método adecuado e imprime el resultado.

text = "12345"
print(text.isnumeric())