def bank(a, years):
    for el in range(int(years)):
        a *= 1.1
    return round(a, 2)


print(bank(1000, 4))