def is_prime(x):
    my_list = []
    for el in range(2, x // 2 + 1):
        if x % el == 0:
            my_list.append(el)
    if len(my_list) == 0:
        return True
    else:
        return False


print(is_prime(997))
