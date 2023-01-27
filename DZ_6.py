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
str1 = input('Введите первую строку: ')
str2 = input('Введите вторую строку: ')
str3 = input('Введите третью строку: ')
str4 = input('Введите четвертую строку: ')
file_x = open('1.txt', 'w')
file_x.write(str1 + '\n')
file_x.write(str2 + '\n')
file_x.close()
file_x1 = open('1.txt', 'a')
file_x1.write(str3 + '\n')
file_x1.write(str4 + '\n')
file_x1.close()