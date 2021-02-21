def square(x):

    p = x * 4
    s = x * x
    d = x * 1.4142135623730951
    return f'Площадь: {p}, периметр: {s}, длина диаонали: {round(d, 3)}'


print(square(5))