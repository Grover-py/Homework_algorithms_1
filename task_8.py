year_user = int(input('Введите год: '))

if year_user % 4 == 0:
    if year_user % 100 == 0 and year_user % 400 != 0:
        print('Год НЕ является високосным')
    else:
        print('Год является високосным')
else:
    print('Год НЕ является високосным')
