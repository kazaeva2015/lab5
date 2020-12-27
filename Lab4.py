import csv
import glob
import os

class Collection(object):
    """ Класс объекта Collection """
    def __init__(self, code, name, count, pay, number):
        """ Конструктор ообъекта класса
        Есть класс Collection, объекты которого должны иметь артикул, название, кол-во, цену и номер;
        self - ссылка на сам созданный объект
        остальные значения будут присвоены параметрам этого метода """
        self.code = code
        self.name = name
        self.count = count
        self.pay = pay
        self.number = number

    def __setattr__(self, attr, value):
        """ Устанавливает значение атрибута указанного объекта по его имени
        attr - имя(ключ)
        value - значение """
        if attr == 'code':
            self.__dict__[attr] = value
        elif attr == 'name':
            self.__dict__[attr] = value
        elif attr == 'count':
            self.__dict__[attr] = value
        elif attr == 'pay':
            self.__dict__[attr] = value
        elif attr == 'number':
            self.__dict__[attr] = value
        else:
            raise AttributeError

    def __repr__(self):
        """ Возвращает строку, которая содержит печатаемое формальное представление объекта,
        которое можно использовать для воссоздания точно такого же объекта;
        join - метод строки, с помощью которого можно вывести в одну строку соединенные элементы
        списка, при этом между элементома вставляется разделитель"""
        return "code: " + self.code.join(("'", "'")) + " name: " + self.name.join(("'", "'")) + " count: " + self.count.join(("'", "'")) + " pay: " + self.pay.join(("'", "'")) + " number: " + self.number.join(("'", "'"))


class Editor:
    """ Статические методы """
    @staticmethod
    def count_file():
        """ Кол-во файлов в папке """
        files = os.listdir(path=".")  # папка, в которой находится лабораторная работа
        print("В папке c проектом " + str(len(files)) + " файлов")

    @staticmethod
    def read():
        """ Чтение из файла
        param: arr
        return: arr """
        arr = []
        with open("x.csv", "r", encoding='utf-8') as r_file:
            file = csv.DictReader(r_file, delimiter=";")
            for row in file:
                k = Collection(row['code'], row['name'], row['count'], row['pay'], row['number'])
                arr.append(k)
            return arr


class Process(Editor):
    def __init__(self, perem):
        self.perem = perem

    def __repr__(self):
        """ str() - возвращает объект в неформальном строков предствлении """
        return str(self.perem)

    def __getitem__(self, i):
        """ Доступ по индексу (ключу) """
        return self.perem[i]

    def sort(self):
        """Сортировка списка по названию
        lambda - определяет функции, которые являются объектами функций, объявленный с помощью def;
        name: - аргумент (ключ)
        name.name - возвращаемое значение """
        self.perem = sorted(self.perem, key=lambda name: name.name)
        self.prints()

    def prints(self):
        """Вывод данных"""
        objs = iter(self) # получение итератора - объекта, который можно перебирать
        while True:
            try:
                print(next(objs)) # получение доступа к элементам
            except StopIteration:
                break
        print('\n')

    def select(self):
        """Выборка строк, где цена равна 16"""
        for elem in self:
            if int(elem.pay) == 16:
                print(elem)
        print('\n')


def begin():
    """Главная функция"""
    table = Process.read()
    table2 = Process(table)
    print("Нажмите 1, чтобы посчитать кол-во файлов в папке с лабораторной")
    print("Нажмите 2, чтобы увидеть все записи в файле")
    print("Нажмите 3, чтобы сортировать строки по алфавиту (по названию)")
    print("Нажмите 4, чтобы сделать выборку")
    while True:
        var = input()
        if var == "1":
            Process.count_file()
        elif var == "2":
            table2.prints()
        elif var == "3":
            table2.sort()
        elif var == "4":
            table2.select()
        else:
            print("Программа работу закончила")
            break


begin()
