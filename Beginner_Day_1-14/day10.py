def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 4 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False

print(is_leap_year(1989))

