# Clase en vídeo: https://youtu.be/TbcEqkabAWU

### Dates ###

# Date time

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

now = datetime.now()


def print_date(date):
    print(f"Date: {date}")
    print(f"Year: {date.year}")
    print(f"Month: {date.month}")
    print(f"Day: {date.day}")
    print(f"Hour: {date.hour}")
    print(f"Minute: {date.minute}")
    print(f"Second: {date.second}")
    print(f"Timestamp: {date.timestamp()}")
print("\nEmepzamos a trbajar con datetime\n")
print_date(now)

year_2025 = datetime(2025, 12, 25)

print_date(year_2025)

print("\nEmepzamos a trbajar con time\n")

# Time


current_time = time(21, 6, 0)

print(f"Time: {current_time}")
print(f"Hour: {current_time.hour}")
print(f"Minute: {current_time.minute}")
print(f"Second: {current_time.second}")



print("\nEmepzamos a trbajar con date\n")
# Date

current_date = date.today()

print(f"año de la current_date = date.today(): {current_date.year}")
print(f"mes de la current_date = date.today(): {current_date.month}")
print(f"dia de la current_date = date.today(): {current_date.day}")

current_date = date(2025, 8, 30)

print(f"año de la current_date = date(2025, 8, 30): {current_date.year}")
print(f"mes de la current_date = date(2025, 8, 30): {current_date.month}")
print(f"dia de la current_date = date(2025, 8, 30): {current_date.day}")

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print(f"mes de la current_date = date(current_date.year, current_date.month + 1, current_date.day): {current_date.month}")

# Operaciones con fechas

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


start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(f"end_timedelta - start_timedelta: {end_timedelta - start_timedelta}")
print(f"end_timedelta + start_timedelta: {end_timedelta + start_timedelta}")

print("\nFIN\n")
