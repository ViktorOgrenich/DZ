import sqlite3
# 1 Создать таблицу со студентами в БД
# 2 Создать таблицу аудиторий в БД
# 3 Сделать связь таблиц

table = sqlite3.connect('students.db')
cur = table.cursor()
cur.execute("PRAGMA foreign_keys=ON")


cur.execute("""CREATE TABLE Students (ID INTEGER PRIMARY KEY NOT NULL,
                                       First_name TEXT KEY NOT NULL,
                                       Last_name TEXT,
                                       Age INTEGER,
                                       Sex TEXT)""")

cur.execute("""CREATE TABLE Room (RoomID INTEGER PRIMARY KEY NOT NULL,
                                       RoomNum INTEGER,
                                       Sex TEXT,
                                       FOREIGN KEY (Sex) REFERENCES Students (Sex))""")

cur.execute("""INSERT INTO Room (RoomID, RoomNum, Sex)
                                      VALUES (1, 203, 'male'),
                                             (2, 205, 'famele')""")

cur.execute("""INSERT INTO Students (ID, First_name, Last_name, Age, Sex)
                                     VALUES (1, 'John', 'Way', 28, 'male'),
                                            (2, 'Mary', 'Jane', 32, 'famale'),
                                            (3, 'Kevin', 'Nourus', 36, 'male'),
                                            (4, 'Anna', 'Rane', 29, 'famale'),
                                            (5, 'Vincent', 'Vega', 29, 'male'),
                                            (6, 'Janin', 'Vain', 22, 'famale'),""")

table.commit()

all_male = cur.execute("""SELECT Students.First_name, Students.Last_name, Room.RoomNum 
                         FROM Students, Room
                         WHERE Students.Sex == Room.Sex""")

for x in all_male: print(f'Фамилия: {x[0]} | Имя: {x[1]} | номер кабинета: {x[2]} | Пол: {x[3]}')
