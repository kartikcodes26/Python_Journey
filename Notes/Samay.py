import time
import os
from datetime import datetime, timedelta
from datetime import date

start = time.time()
print("Starting in : ")
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("Go")
time.sleep(1)
end = time.time()
print(f"Time Taken : {(end - start):.2f} seconds")

while True:
    os.system("cls")
    print(datetime.now())
    time.sleep(1)
    
now = datetime.now()
deadline = date(2026, 12, 6)
print(deadline)

# %A: Full weekday name (e.g., Wednesday)
# %B: Full month name (e.g., June)
# %d: Day of the month (e.g., 24)
# %Y: 4-digit year (e.g., 2026)

print(now.strftime("%A, %B, %d, %Y"))

print((now + timedelta(days = 10)).strftime("%A, %B, %d, %Y"))
print((now - timedelta(days = 10)).strftime("%A, %B, %d, %Y"))


    

