def is_leap_year(year):
    if (year % 1 != 0 or year <= 0):
        return False
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
            return True
        return False


print(is_leap_year(2000))  # True
print(is_leap_year(-2024))  # False
print(is_leap_year(1984.25))  # False
