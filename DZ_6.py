import json
import random
import csv

# 6.1 декодировать в строку байтовое значение

a = b'r\xc3\xa9sum\xc3\xa9'
print(a)
b = a.decode('utf-8')
print('utf-8: ', b)
c = b.encode('Latin1')
print('Latin1: ', c)
d = c.decode('Latin1')
print('Latin1: ', d)

# 6.2 ввести 4 строки, сохранить в 4 переменные, записать в файл
str1 = str(random.randint(100, 9999))
str2 = str(random.randint(100, 9999))
str3 = str(random.randint(100, 9999))
str4 = str(random.randint(100, 9999))
file_x = open('1.txt', 'w')
file_x.write(str1 + '\n' + str2 + '\n')
file_x.close()
file_x = open('1.txt', 'a')
file_x.write(str3 + '\n' + str4 + '\n')
file_x.close()

# 6.3 создать словарь с ключем id, значения кортеж из двух состовляющих name(str), age(int)

name = ("Mike", "Anna", "Germes", "Bond", "Adolf")
age = (34, 45, 53, 23, 65)
prime = {(999999-n):(name[n], age[n]) for n in range(5)}
with open ('ttes.json', 'w') as file_y:
    json.dump(prime, file_y)
    file_y.close()
5
#6.4 прочитать сохраненный файл, и записать данные на диск в csv-файл, первой строкой озаглавив каждый столбец,
# и добавить новый столбец "телефон"

with open('ttes.json', 'r') as file_y:
    temp_f = json.load(file_y)
    file_y.close()

temp_e = [[key, temp_f[key][0], temp_f[key][1],
         ("+37529" + str(random.randint(1000000, 9999999)))]
        for key in temp_f]
with open('ttes.csv', 'w') as file_r:
    writer = csv.writer(file_r)
    writer.writerow(['ID', 'NAME', 'AGE', 'PHONE'])

    for line in temp_e:
        writer.writerow(line)
    file_r.close()
print(temp_f)
print(temp_e)

#6.5 прочитать csv-файл и сохранить данные в excel файл, кроме возраста.
with open('ttes.json', 'r') as file_y:
    temp_f = json.load(file_y)
    file_y.close()





