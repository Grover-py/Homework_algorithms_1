def my_date(d, m, y):
    import datetime
    try:
        x = datetime.date(y, m, d)
        return True
    except:
        return False


print(my_date(10, 22, 1995))
