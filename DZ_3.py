# 3.1 форматирование строки

first = input('Введите первое слово: ')
second = input('Введите второе слово: ')

offer = first + ' ' + second
print(offer)
offer = offer.reverse()
offer1 = second + ' ' + first
offer2 = '!' + second + ' ! ' + first + '!'

print(offer)
print(offer1)
print(offer2)


@ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @

# программа проверки возраста юзера 3.2, 3.3


while True:
    name = input('Введите имя персонажа: ')
    age = input('Введите возраст персонажа: ')
    while not age.isdigit():
        print('Ошибка, повторите ввод ')
        age = input('Введите возраст персонажа: ')
    if int(age) <= 0:
        print('Ошибка, повторите ввод ')
    elif int(age) > 0 and int(age) < 10:
        print('Привет, шкет', name)
    elif int(age) >= 10 and int(age) <= 18:
        print('Как жизнь', name, '?')
    elif int(age) > 18 and int(age) < 100:
        print('Что желаете', name, '?')
    else:
        print(name, 'Вы лжете, в наше время столько не живут', )


@ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @

# 3.4 сумма кубов


n = input('Введите число n: ')
n = int(n)
s = 0
for i in range(1, n + 1):
    s += i ** 3

print(s)

n = input('Введите число n: ')
n = int(n)
s = 0
r = 1
while r != n + 1:
    s += r ** 3
    r += 1

print(s)


@ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @

# 3.5  программа угадывания числа


import random

n = 10
rand_num = random.randint(1, n)

m = int(input('По-пробуйте угадать число: '))
print(m)
print(n)
if n == m:
    print('Поздравляю, вы угадали число ')
else:
    print('Увы, вы не угадали число ')