# Clase en vídeo: https://youtu.be/TbcEqkabAWU

### Dates ###

# Date time

# Importamos las clases necesarias del módulo datetime
from datetime import timedelta # Para trabajar con franjas de tiempo (diferencias)
from datetime import date # Para trabajar con fechas (año, mes, día)
from datetime import time # Para trabajar con horas (hora, minuto, segundo)
from datetime import datetime # Para trabajar con fecha y hora juntas

# datetime.now() nos da la fecha y hora actual exacta del sistema
now = datetime.now()


def print_date(date):
    """Función auxiliar para imprimir los componentes de un objeto fecha/hora"""
    print(f"Date: {date}")
    print(f"Year: {date.year}")       # Accedemos al año
    print(f"Month: {date.month}")     # Accedemos al mes
    print(f"Day: {date.day}")         # Accedemos al día
    print(f"Hour: {date.hour}")       # Accedemos a la hora
    print(f"Minute: {date.minute}")   # Accedemos a los minutos
    print(f"Second: {date.second}")   # Accedemos a los segundos
    print(f"Timestamp: {date.timestamp()}") # Representación numérica del tiempo (segundos desde 1970)

print("\nEmepzamos a trbajar con datetime\n")
print_date(now)

# Podemos crear una fecha específica pasando (año, mes, día)
year_2025 = datetime(2025, 12, 25)

print_date(year_2025)

print("\nEmepzamos a trbajar con time\n")

# Time

# Creamos un objeto de tiempo específico (hora, minuto, segundo)
current_time = time(21, 6, 0)

print(f"Time: {current_time}")
print(f"Hour: {current_time.hour}")
print(f"Minute: {current_time.minute}")
print(f"Second: {current_time.second}")



print("\nEmepzamos a trbajar con date\n")
# Date

# date.today() nos da solo la fecha actual (sin hora)
current_date = date.today()

print(f"año de la current_date = date.today(): {current_date.year}")
print(f"mes de la current_date = date.today(): {current_date.month}")
print(f"dia de la current_date = date.today(): {current_date.day}")

# Creamos una fecha específica con date()
current_date = date(2025, 8, 30)

print(f"año de la current_date = date(2025, 8, 30): {current_date.year}")
print(f"mes de la current_date = date(2025, 8, 30): {current_date.month}")
print(f"dia de la current_date = date(2025, 8, 30): {current_date.day}")

# Podemos crear una nueva fecha basándonos en los datos de otra
current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print(f"mes de la current_date = date(current_date.year, current_date.month + 1, current_date.day): {current_date.month}")

# Operaciones con fechas

# Al restar dos fechas, obtenemos un objeto 'timedelta' que representa la duración entre ellas
diff = year_2025 - now
print(f"diff = year_2025 - now: {diff}")

diff = year_2025.date() - current_date
print(f"diff = year_2025.date() - current_date: {diff}")

print(f"current_date = date(current_date.year, current_date.month + 1, current_date.day): {current_date}")

dia_beso = datetime(2025, 8, 31)

print(f"dia_beso = datetime(2025, 8, 31): {dia_beso}")
diff =  dia_beso - now
print(f"diff = dia_beso - now: {diff}")

print("\nEmepzamos a trbajar con timedelta\n")
# Timedelta

# definimos franjas de tiempo para sumar o restar
start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

# Podemos sumar o restar tiempos
print(f"end_timedelta - start_timedelta: {end_timedelta - start_timedelta}")
print(f"end_timedelta + start_timedelta: {end_timedelta + start_timedelta}")

print("\nFIN\n")
