from datetime import datetime


def format_timestamp_with_commas(x, floating_number: int):
    """
    Formats an integer with commas as thousand separators.
    """
    formatted_number = f"{x:,}"
    index_point = formatted_number.find(".")
    if (index_point == -1 or floating_number <= 0):
        return formatted_number
    return formatted_number[0:(index_point + floating_number + 1)]


if __name__ == "__main__":
    current_time = datetime.now()
    timestamp_curr_time = current_time.timestamp()
    formatted_timestamp = format_timestamp_with_commas(timestamp_curr_time, 4)

    print(f"Seconds since January 1, 1970: {formatted_timestamp} or\
    {timestamp_curr_time:.2e} in scientific notation")
    print(current_time.strftime("%b %d %Y"))
