a = str(input('Operation: '))
b = float(input('Первое число: '))
c = float(input('Second number: '))

if a == '+':
    d = b + c
elif a == '-':
    d = b - c
elif a == '*':
    d = b * c
else:
    d = b / c

print(b, a, c, '=', d)