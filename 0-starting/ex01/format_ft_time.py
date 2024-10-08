import time as time
from datetime import datetime

curr_time_value = datetime.now()

full_format = "1,666,355,857.3622" # Except
scientific_notation_format = "1.67e+09" # Except
current_time = "Oct 21 2022" # Except

timestamp_current_time = curr_time_value.timestamp()
# print(time.time())
print(timestamp_current_time)
print(f"Seconds since January 1, 1970: {full_format} or {scientific_notation_format} in scientific notation")

print("EXCEPT")
print(current_time)
print("MINE")
print(curr_time_value.strftime("%b %d %Y"))
# time.
