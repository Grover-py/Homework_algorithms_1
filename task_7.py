
my_list = []

my_list.append(float(input('Введите первую сторону треугольника: ')))
my_list.append(float(input('Введите вторую сторону треугольника: ')))
my_list.append(float(input('Введите третью сторону треугольника: ')))

my_list.sort(reverse = True)

if my_list[0] >= my_list[1] + my_list[2]:
    print('Треугольник с такими сторонами невозможен')
elif my_list[0] == my_list[1] == my_list[2]:
    print('Ваш треугольник, равносторонний')
elif my_list[0] == my_list[1] or my_list[1] == my_list[2]:
    print('Ваш треугольник, равнобедренный')
elif my_list[0] ** 2 == my_list[1] ** 2 + my_list[2] ** 2:
    print('Ваш треугольник, прямоугольный')
else:
    print('Ваш треугольник, разносторонний')

