# Lesson 10 — seconds since 1 January 1970
from time import time, ctime

current_time = time()
print(current_time)
print(ctime(current_time))

seconds_in_a_year = 365.25 * 24 * 60 * 60
years_since_1970 = current_time / seconds_in_a_year
print(years_since_1970)
print("Seconds in a day:", 24 * 60 * 60)
