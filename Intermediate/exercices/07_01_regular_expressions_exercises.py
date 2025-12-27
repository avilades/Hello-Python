
import re

# 1. Busca si una cadena empieza por "Hola".
string = "Hola, ¿cómo estás?"
pattern = r"^Hola"
match = re.match(pattern, string)
print(match)

# 2. Busca la palabra "Python" en una cadena aunque esté en minúsculas.
string = "Hola, ¿cómo estás?, aprendes python"
pattern = "python"
match = re.search(pattern, string, re.I)
start, end = match.span()
print(match)
print(f"las posiciones de match son: {match.span()}")
print(f"el texto encontrado es (match.group()): {match.group()}")
print(f"el texto encontrado es (match.group(0)): {match.group(0)}")
print(f"el texto encontrado es (string[start:end]): {string[start:end]}")


# 3. Encuentra todas las apariciones de la palabra "curso" en una cadena.
string = "Hola, ¿que talv a el curso de python?, te gustaria hacer algun otro curso cuando realices el curso de python"
pattern = r"curso"
match = re.findall(pattern, string)
print(match)

# 4. Reemplaza todas las apariciones de "lección" por "LECCIÓN".
string = "Hola, ¿cómo llevas la lección de python? Cuando crees que empezaras la siguiente Lección"
pattern = r"lección"
match = re.sub(pattern, "LECCIÓN", string)
print(match)

pattern = r"[lL]ección"
match = re.sub(pattern, "LECCIÓN", string)
print(match)

# 5. Divide un texto en partes separadas por comas.
string = "Es, una cadena, con varias, comas, para probar, ¿cómo estás?"
pattern = r" "
match = re.split(pattern, string)
print(match)

pattern = r","
match = re.split(pattern, string)
print(match)

# 6. Busca la primera palabra que comience con "A" o "a".
string = "Hola, ¿cómo estás?"
pattern = r"curso"
match = re.match(pattern, string)
print(match)

# 7. Encuentra todas las palabras en una cadena que terminen en "ción".
string = "Hola, ¿cómo estás?"
pattern = r"curso"
match = re.match(pattern, string)
print(match)

# 8. Verifica si una cadena contiene solo números.
string = "Hola, ¿cómo estás?"
pattern = r"curso"
match = re.match(pattern, string)
print(match)

# 9. Reemplaza todos los números de una cadena por el texto "[número]".
string = "Hola, ¿cómo estás?"
pattern = r"curso"
match = re.match(pattern, string)
print(match)

# 10. Encuentra todas las palabras de 4 letras exactas en una cadena.