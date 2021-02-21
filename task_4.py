def season(month):
    season_l = ['Зима', 'Весна', 'Лето', 'Осень']
    if month == 12 or month == 1 or month == 2:
        return season_l[0]
    elif 3 <= month <= 5:
        return season_l[1]
    elif 6 <= month <= 8:
        return season_l[2]
    elif 9 <= month <= 11:
        return season_l[3]
    else:
        print('В году всего 12 месяцев')


print(season(12))