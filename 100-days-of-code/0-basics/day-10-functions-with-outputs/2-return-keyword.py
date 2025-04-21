def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("jOhn", "doe"))


# Coding excersise
def is_leap_year(year):
    """This function takes a year as input and returns True if it is a leap year, otherwise False.""" # Docstring
    # A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
    is_leap_year = False
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                is_leap_year = True
        else:
            is_leap_year = True
    return is_leap_year

print(is_leap_year(2400))
