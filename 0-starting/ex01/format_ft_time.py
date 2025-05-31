from datetime import datetime


# full_format = "1,666,355,857.3622"  # Except
# scientific_notation_format = "1.67e+09"  # Except
# current_time = "Oct 21 2022"  # Except

# print("==== EXCEPT ====")
# print(f"Seconds since January 1, 1970: {full_format} or\
#  {scientific_notation_format} in scientific notation")
# print(current_time)


def format_int_with_commas(x, floating_number: int):
    """
    Formats an integer with commas as thousand separators.
    """
    formatted_number = f"{x:,}"
    index_point = formatted_number.find(".")
    if (index_point == -1 or floating_number <= 0):
        return formatted_number
    return formatted_number[0:(index_point + floating_number + 1)]


# print("==== MINE ====")
current_time = datetime.now()
timestamp_current_time = current_time.timestamp()
formatted_timestamp = format_int_with_commas(timestamp_current_time, 4)

print(f"Seconds since January 1, 1970: {formatted_timestamp} or\
 {timestamp_current_time:.2e} in scientific notation")
print(current_time.strftime("%b %d %Y"))
