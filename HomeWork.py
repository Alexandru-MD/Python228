########################## Рекурсия ######################################
# def count(numbers):
#     if len(numbers) == 0:
#         return 0
#     else:
#         cnt = count(numbers[1:])
#         if numbers[0] < 0:
#             cnt += 1
#         return cnt
# nums = [-2, 3, 8, -11, -4, 6]
# print("Количество отрицательных чисел: ", count(nums))

################### ООП методы и свойства. Задача #########################
# class Car:
#     model = 'model'
#     year = 'year'
#     producer = 'producer'
#     motor = "motor"
#     colour = 'colour'
#     price = 'price'
#
#     def print_info(self):
#         print("Данные автомобиля".center(40, '*'))
#         print(f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.producer}\nМощность "
#               f"двигателя: {self.motor}\nЦвет машины: {self.colour}\nЦена: {self.price}")
#         print("=" * 40)
#
#     def input_info(self, model, year, producer, motor, colour, price):
#         self.model = model
#         self.year = year
#         self.producer = producer
#         self.motor = motor
#         self.colour = colour
#         self.price = price
#
#     def set_model(self, model):
#         self.model = model
#
#     def get_model(self):
#         return self.model
#
#     def set_year(self, year):
#         self.year = year
#
#     def get_year(self):
#         return self.year
#
#     def set_producer(self, producer):
#         self.producer = producer
#
#     def get_producer(self):
#         return self.producer
#
#     def set_motor(self, motor):
#         self.motor = motor
#
#     def get_motor(self):
#         return self.motor
#
#     def set_colour(self, colour):
#         self.colour = colour
#
#     def get_colour(self):
#         return self.colour
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
#
# info = Car()
# info.input_info("X7 M50i", "2021", "BMW", "530 л.с.", "White", 10790000)
# info.print_info()
# info.set_model("M5")
# info.set_year("2018")
# info.set_producer('Ferrari')
# info.set_motor("780 л.с.")
# info.set_colour("Оранжевый")
# info.set_price("25000000")
# # info.get_model()
# info.print_info()
# class Person:
#     name = "name"
#     surname = "surname"
#     qualification = 'qualification'
#
#     def print_info(self):
#         print()
#         print(f"Данные сотрудника: {self.name} {self.surname}\nКвалификация сотрудника: {self.qualification}")
#         print()
#
#     def input_info(self, name, surname, qualification):
#         self.name = name
#         self.surname = surname
#         self.qualification = qualification
#
#     def set_name_surname(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def get_name_surname(self):
#         return self.name, self.surname
#
#     def set_qualification(self, qualification):
#         self.qualification = qualification
#
#     def get_qualification(self):
#         return self.qualification
#
#
# info = Person()
# info.input_info("Александр", "Спринсиян", 13)
# info.print_info()
# info.set_name_surname("Анна", "Долгих")
# info.set_qualification(12)
# info.print_info()
# ======================================================================================================================

# ======================================================================================================================
# class Student:
#     def __init__(self):
#         self.name = "Roman"
#         self.info = self.Info()
#
#     def info_name(self):
#         print("Name: ", self.name)
#
#     class Info:
#         def __init__(self):
#             super().__init__()
#             self.brand = "HP"
#             self.processor = "I7"
#             self.ram = "16 GB"
#
#         def show(self):
#             print("Name: ", Student.info_name(), "->", self.brand, self.processor, self.ram)
#
#
# s = Student()
# # s.info_name()
# i = s.info
# i.show()
# ================================  Скрещивание котов ==================================================================
# import random
#
#
# class Cat:
#     def __init__(self, name, pol):
#         self.name = name
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age=0, sex={self.pol})"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", random.choice(["F", "M"])) for _ in range(random.randint(1, 5))]
#         else:
#             return "Как ты себе представляешь скрестить мальчика с мальчиком? Кого хочешь получить?"
#
#
# cat1 = Cat("Tom", 'M')
# print(cat1)
# cat2 = Cat("Elza", "F")
# print(cat2)
# print(cat1 + cat2)
# cat3 = Cat("Ron", "M")
# print(cat3)
# print(cat1 + cat3)
# ======================================================================================================================
# class Power:
#     def __init__(self, degree):
#         self.degree = degree
#
#     def __call__(self, fn):
#         def wrap(a, b):
#             print("Результат: ", fn(a, b) ** self.degree)
#
#         return wrap
#
#
# # @Power(3)
# def func(a, b):
#     return a * b
#
#
# # func(2, 2)
# test = Power(3)
# test1 = test(func)
# test1(2, 2)
# ======================================================================================================================

# ======================================================================================================================
######################################    Основной принцип написания дескриптора ######################################
# class Integer:  # Деструктор
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int) or coord < 0:
#             raise TypeError(f"Координата {coord} должна быть целым числом, и не отрицательным!")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)  # Аналог
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)  # Аналог
#
#     def __delete__(self, instance):
#         # del instance.__dict__[self.name]
#         delattr(instance, self.name)                            # Аналог
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# del p1.x
# p1.x = 5
# print(p1.__dict__)
#################     Существование треугольников
# class Integer:
#     @staticmethod
#     def verify(coord):
#         if coord < 0:
#             raise ValueError("Сторона не может быть отрицательной!")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify(value)
#         setattr(instance, self.name, value)
#
#
# class Point:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def is_valid(self):
#         return self.x + self.y > self.z and \
#                self.x + self.z > self.y and \
#                self.y + self.z > self.x
#
#
# p1 = Point(2, 5, 6)
# p2 = Point(5, 2, 8)
# p3 = Point(7, 3, 6)
# # print("Первый треугольник:", p1.__dict__)
# # print("Второй треугольник:", p2.__dict__)
# # print("Третий треугольник:", p3.__dict__)
# p_all = [p1, p2, p3]
# for info in p_all:
#     if info.is_valid():
#         print(f"Треугольник со сторонами ({info.x}, {info.y}, {info.z}) существует!")
#     else:
#         print(f"Треугольник со сторонами ({info.x}, {info.y}, {info.z}) не существует!")
# =======================================================================================================================

# =======================================================================================================================
import json

data = {}


class Countries:
    def __init__(self, country, town):
        self.country = country
        self.town = town
        data[self.country] = self.town

    def __str__(self):
        return f"{data}"

    def add_data(self, key, value):
        if key in data:
            data[key] = value

    def remove_ctr(self, key):
        if key in data:
            del data[key]

    def change_town(self, key, new_value):
        if key in data:
            data[key] = new_value

    def get_value(self, key):
        return data.get(key)


print('*' * 30)
print("Выбор действия:")
c = Countries('Russia', 'Moscow')
print(c)
while c != 6:
    input('Введите значение')
    if c == 1:
        c.add_data(input("Введите данные"))
        input('Введите значение')
    if c == 2:
        c.remove_ctr(input("Введите данные"))
        input('Введите значение')
    if c == 3:
        c.remove_ctr(input("Введите данные"))
        input('Введите значение')
    if c == 4:
        c.change_town(input("Введите данные"))
        input('Введите значение')
    if c == 5:
        c.get_value(input("Введите данные"))
        input('Введите значение')
    if c == 6:
        print("Программа завершена")
