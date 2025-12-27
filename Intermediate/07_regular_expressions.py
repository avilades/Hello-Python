# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=19762

### Regular Expressions ###

import re

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

# match: intenta encontrar el patron SOLO al principio de la cadena
# re.I: hace que la búsqueda sea insensible a mayúsculas y minúsculas 
match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Expresiones Regulares", my_string))

# search

# search: busca el patrón en toda la cadena (no solo al principio)
search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

# findall: encuentra TODAS las ocurrencias del patrón y las devuelve en una lista
findall = re.findall("lección", my_string, re.I)
print(findall)

# split

# split: divide la cadena en cada ocurrencia del patrón
print(re.split(":", my_string))

# sub

# sub: reemplaza las ocurrencias del patrón por otro texto
print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

### Regular Expressions Patterns ###

# Para aprender y validar expresiones regulares: https://regex101.com

# Patrones personalizados
pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

# [lL]ección|Expresiones: encuentra todas las ocurrencias del patrón, en este caso "lección" o "Expresiones"
# [lL]: encuentra todas las ocurrencias del patrón, en este caso "l" o "L"
# |: encuentra todas las ocurrencias del patrón, en este caso "lección" o "Expresiones"                  
pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

# [0-9]: encuentra todos los dígitos
pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

# \d: encuentra todos los dígitos
pattern = r"\d"
print(re.findall(pattern, my_string))

# \D: encuentra todos los no dígitos
pattern = r"\D"
print(re.findall(pattern, my_string))

# \s: encuentra todos los espacios
pattern = r"\s"
print(re.findall(pattern, my_string))

# \S: encuentra todos los no espacios
pattern = r"\S"
print(re.findall(pattern, my_string))

# \w: encuentra todos los caracteres alfanuméricos
pattern = r"\w"
print(re.findall(pattern, my_string))

# \W: encuentra todos los no caracteres alfanuméricos
pattern = r"\W"
print(re.findall(pattern, my_string))

# [l].*: encuentra todos los que empiecen con l y sigan con cualquier caracter
pattern = r"[l].*"
print(re.findall(pattern, my_string))

# Validación de email
email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))

