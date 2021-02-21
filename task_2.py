def is_year_leap(y):
    import datetime
    try:
        x = datetime.date(y, 2, 29)
        return True
    except:
        return False


print(is_year_leap(2020))
print(is_year_leap(2021))


def is_year_leap_2(y):
    my_list = [el for el in range(0,10000,4)]
    while True:
        if y in my_list:
            return True
        else:
            return False

print(is_year_leap_2(2020))
print(is_year_leap_2(2021))
