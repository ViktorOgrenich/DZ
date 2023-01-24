import datetime
import time

#4.1 поменять местами ключи и значения из начального словаря
sl1 = {'x':10, 'y':20, 'z':30}
print('Начальный словарь: \n', sl1)
sl2 = {v: k for k, v in sl1.items()}
print('Исправленый словарь: \n', sl2)

#4.2 найти факториал
n = input('Введите число: ')
n = int(n)
def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n

print('Факториа числа', n,':\n', fact(n))

#4.3 список чисел, поситать количество каждого числа

numb = input('Введите произвольный набор цифр: ')
x = [int(a) for a in str(numb)]
def num_calc(x):
    num = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '0': 0 }
    for i in x:
        if i == 1:
            num['1'] += 1
        elif i == 2:
            num['2'] += 1
        elif i == 3:
            num['3'] += 1
        elif i == 4:
            num['4'] += 1
        elif i == 5:
            num['5'] += 1
        elif i == 6:
            num['6'] += 1
        elif i == 7:
            num['7'] += 1
        elif i == 8:
            num['8'] += 1
        elif i == 9:
            num['9'] += 1
        else:
            num['0'] += 1
    return(num)
print(num_calc(x))

# 4.4 сделать функцию которая вызывается из генератора списков, и по запросу к ней отдавать текущее время -1с
from datetime import datetime
i = int(input('Введите количество записей в списке: '))

def now():
    return datetime.strftime(datetime.now(), "%Y/%m/%d %H:%M:%S")

t_d_nuw = []
while i != 0:
    time.sleep(1)
    t_d_nuw += [now()]
    i -= 1
print(t_d_nuw)

