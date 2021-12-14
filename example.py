def max_num(num_1, num_2):
    maxx = (num_1 + num_2) / 2 + abs((num_1 - num_2) / 2)
    return maxx

x_1 = float(input('Введите первое число: '))
x_2 = float(input('Введите второе число: '))
x_3 = float(input('Введите третье число: '))

max_1 = max_num(x_1, x_2)
max_2 = max_num(max_1, x_3)
print('Наибольшее из трёх чисел: ', max_2)