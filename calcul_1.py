a = str(input('Operation: '))
x = int(input('How operand? '))
b = int(input('Input number 1: '))
for n in range(2, x + 1):
    print('Input number ', n, ': ', sep='', end = '')
    c = int(input())    
    if a == '+':
        d = b + c
        b = d
    elif a == '-':
        d = b - c
        b = d
    elif a == '*':
        d = b * c
        b = d
    else:
        d = b / c
        b = d
print(d)