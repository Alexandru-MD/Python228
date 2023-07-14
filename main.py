# name = "Alex"
# print("Hello", name)
# age = 20
# print(age)
# print(type(name))
# print(type(age))
# a = 4
# b = 5
# a = b
# print(id(a))  # id
# print(id(b))
# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, "Hello", 9.2
# print(a, b, c)

# _name_2 = "Bob"
# print(_name_2)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = "Hello"
# print(type(a))
# a = 3
# print(type(a))

# name = "Alex"
# age = 24
# print("Меня зовут: " + name + ". Мне " + str(age) + " года")

# a = 1
# b = 2
# print("a: ", a)
# print("b: ", b)

# c = a
# a = b
# b = c

# a, b = b, a

# print("a: ", a)  # 2
# print("b: ", b)  # 1

# print("строка \
# символов")
# print('строка '
#       'символов')

# print("Документ \"script.py\" находится  по заданному пути \nC:\\\Python and other\\Projects")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", "+ s2 + "!\t\t"
# print(s3 * 3)
# print("*"*40)

# print(4334242424242424)

# print(6 + 2)
# print(6 * 2)
# print(6 / 2)
# print(8 / 2)
# print(6 // 2)
# print(6 % 2)
# print(6 ** 2)

# a = 5
# b = 7
# c = 3
# suma = (a + b + c)
# Umnojenie = (a * b * c)
# Arifmeticheskoe = (a + b + c)/3
# print("Сумма: " + str(suma))
# print("Произведение: " + str(Umnojenie))
# print("Среднее арифметическое: " + str(Arifmeticheskoe))

# num = 10
# num += 5
# print(num)

# num = 4321
# a = num % 10
# print(a)
# num = num // 10
# # print(num)
# b = num % 10
# # print(b)
# num = num // 10
# # print(num)
# c = num % 10
# # print(c)
# num = num // 10
# # print(num)
# d = num % 10
# # print(d)
# antinum = a * 1000 + b * 100 + c * 10 + d
# print(antinum)


# num1 = 4321
# print(num1)
# res = (num1 % 10) * 1000
# num1 //= 10
# res+=(num1 % 10) * 100
# print(res)
# num1 //= 10
# res+=(num1 % 10) * 10
# print(res)
# num1 //= 10
# res+=(num1 % 10)
# print(res)

# int() - преобразовывает к числовому типу данных(числа)
# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)

# print(int(3.8))
# print(round(3.82, 2))  #  Количество символов после запятой

# a = 5 / 3
# print(round(a, 2))

# a = '5.2'
# b = 10
# c = float(a) + b
# print(int(c))

# a = 1
# b = 2
# print("a:", a, "\nb:", b)

# name = "Виктор"
# age = 35
# print("Меня зовут: ", name, ".Мне ", age, "лет")
# print("Меня зовут: " + name + ". Мне " + str(age) + " лет")
# print("Меня зовут: ", name, ".Мне ", age, "лет", sep="--", end="!!!")
# print("Я учу пайтон.")

# print("*****Ваши данные*****")
# name = input("Введите ваше имя: ")
# city = input("Введите ваш город: ")
# print(name, city)

# print("Решите задачку")
# chislo = input("Введите число: ")
# stepeni = input("Введите степень: ")
# print(int(chislo) ** int(stepeni))

# print("Введите 4 числа")
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# summa1 = a + b
# c = int(input("Введите третье число: "))
# d = int(input("Введите четвертое число: "))
# summa2 = c + d
# summa = print(int(summa1)/int(summa2))

# a = True
# b = False
# print(a + 5)  # 1 + 5 = 6
# print(b * 5)  # 0 * 6 = 0


# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 != 7)
# print("Привет" < "привет")

# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(9 * 3 <= 7 >= 2)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10, 5, False


# print(5 - 3 == 2 and 1 + 3 == 4)  # (True and True) - True
# print(5 - 3 == 2 and 1 + 3 < 4)  # (True and False) - False
# print(5 - 3 > 2 and 1 + 3 < 4)  # (False and False) - False

# print(5 - 3 == 2 or 1 + 3 == 4)  # (True and True) - True
# print(5 - 3 == 2 or 1 + 3 < 4)  # (True and False) - True
# print(5 - 3 > 2 or 1 + 3 < 4)  # (False and False) - False


# print(not 9 - 9)  # Будет True


# a1 = 15
# if a1 < 10:
#     a1 += 1
# print(a1)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Вы еще малы")

# a = 25
# b = 35
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("b == a")

# print("Решите задачку")
# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
#
# if a == b == c:
#     print("Треугольник равносторонний!")
# elif a == b or a == c or b == c:
#     print("Треугольник равнобедренный!")
# else:
#     print("Треугольник равнобедренный!")

# print("Решите задачку")
# num = int(input("Введите пятизначное число: "))
# a = num % 10
# num = num // 10
# b = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# d = num % 10
# num = num // 10
# e = num % 10
# num = num // 10
# print("Произведение цифр числа: " + str(a * b * c * d * e))
# print("Среднее арифметическое: " + str((a+b+c+d+e)/5))

# print("Решите задачку")
# num = int(input("Напишите число: "))
# if num % 2:
#     print("число нечетное")
# else:
#     print("Число четное")

# print("Калькулятор")
# print("Операции - сложение, вычитание, умножение, деление, процент, булево")
# operatia = input("Выберите операцию: ")
# if operatia == "сложение":
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     print("Сумма элементов: " + str(a + b))
# elif operatia == "вычитание":
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     print("Разность элементов: " + str(a - b))
# elif operatia == "умножение":
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     print("Умножение элементов: " + str(a * b))
# elif operatia == "деление":
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     if b == 0:
#         print("На ноль делить нельзя")
#     else:
#         print("Деление элементов: " + str(a / b))
# elif operatia == "процент":
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     print("Процент деления элементов: " + str(a % b))
# elif operatia == "булево":
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     if a > b:
#         print("Первое число > Второго числа")
#     elif a == b:
#         print("Числа равны, тебе не видно что ли?)")
#     else:
#         print("Первое число < Второго числа")

# print("Все месяца!")
# a = (input("Введите номер месяца: "))
# if a == "1":
#     print("Январь")
# elif a == "2":
#     print("Февраль")
# elif a == "3":
#     print("Март")
# elif a == "4":
#     print("Апрель")
# elif a == "5":
#     print("Май")
# elif a == "6":
#     print("Июнь")
# elif a == "7":
#     print("Июль")
# elif a == "8":
#     print("Август")
# elif a == "9":
#     print("Сентябрь")
# elif a == "10":
#     print("Октябрь")
# elif a == "11":
#     print("Ноябрь")
# elif a == "12":
#     print("Декабрь")
# else:
#     print("Нет такого месяца")

# m = int(input("Введите номер месяца: "))
# if 1 <= m <= 12:
#     if m == 1 or m == 2 or m == 12:
#         print("Зима")
#     elif 3 <= m <= 5:
#         print("Весна")
#     elif 6 <= m <= 8:
#         print("Лето")
#     elif 9 <= m <= 11:
#         print("Осень")
# else:
#     print("Ошибка ввода данных")

# print("Написать слово КОПЕЕК в правильном формате (диапазон от 1 до 99")
# num = int(input("Введите число от 1 до 99: "))
# if 5 <= num <= 20:
#     print(str(num) + " копеек")
# elif num == 1 or
#     print(str(num) + " копейка")
# elif

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # day >= 1 and day <= 5
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник!")
#     if day == 2:
#         print("Вторник!")
#     if day == 3:
#         print("Среда!")
#     if day == 4:
#         print("Четверг!")
#     if day == 5:
#         print("Пятница!")
# elif 6 <= day <= 7:  # day == 6 or day == 7
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота!")
#     if day == 7:
#         print("Воскресенье!")
# else:
#     print("Такого дня недели нету!")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# n = int(input("Введите число от 1 до 99: "))
# koop = n
# if 11 <= koop <= 14:
#     print(n, "копеек")
# else:
#     koop = koop % 10
#     if koop == 1:
#         print(n, "копейка")
#     elif 2 <= koop <= 4:
#         print(n, "копейки")
#     else:
#         print(n, "копеек")

#  Тернарные выражения

# a, b = 10, 20
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# print("a==b" if a == b else ("a > b" if a > b else "b > a"))
#
# if a == b:
#     print("a == b")
# else:
#     if a > b:
#         print("a > b")
#     else:
#         print("b > a")

# a, b = 2, 1
# print("На ноль делить нельзя" if b == 0 else a / b)

#  Исключения
#
# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что то пошло не так!")
# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
# else:     # Когда в блоке try не возникло исключение
#     print("Вы ввели ", n," и ", m)
# finally:  # Выполняется в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
#     m = str(m)
# finally:
#     print(n + m)

# i = 0
# while i < 5:
#     print("i = ", i)
#     i += 1

# i = 10
# while i > 0:
#     print("i = ", i)
#     i -= 1

# i = 1
# while i < 21:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# i = 0
# while i < 20:
#     i += 2
#     print("i", i)

# n = int(input("Введите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Введите количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1

# n1 = int(input("Введите начальный диапазон"))
# n2 = int(input("Введите конечный диапазон"))
# i = 0
# while n1 < n2:
#     if n2 % 3 == 0:
#
#         print("Сумма нечетных чисел")

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное число")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")
# s = 1
# while True:
#     n = int(input("Введите положительное число: "))
#     if n == 0:
#         break
#     s *= n
# print("Результат: ", s)

# i = 0
# while i < 30:
#     if i == 5:
#         break
#     print(i)
#     i+=1
# else:
#     print("Цикл окончен, i=", i)


# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВложенный цикл: j =", j)
#         j += 1
#     i += 1


# i = 1
# while i <= 9:
#     b = 1
#     while b <= 9:
#         print(i, "*", b, "=", i * b, end="\t\t")
#         b += 1
#     print()
#     i += 1


# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 1
# while i <= 5:
#     j = 0
#     while j < 20:
#         if i % 2 != 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#     print(element)


# for i in 'Hello!':
#     print(i)

# i = 1
# for color in 'red', 'orange', 'blue', 2:
#     print(i, "color: ", color, type(color))
#     i += 1

# for i in range(n):
#     тело цикла

# range(start, stop, step)

# for i in range(9, 0):
#     print(i, end=" ")

# print()
# j = 2
# while j < 9:
#     print(j, end=" ")
#     j += 3

# i = int(input("Введите целое число: "))
# for m in range(1, i+1):
#     if i % m == 0:
#         print(m, end=" ")


# for m in range(1, 100):
#     if m % 10 == 0:
#         print(m, end=" ")

# for i in range(3):
#     print(i)
# else:
#     print("Done")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("----")

# visota = int(input("Введите высота прямоугольника: "))
# dlina = int(input("Введите длину прямоугольника: "))
# for i in range(visota):
#     for b in range(dlina):
#         if (0 < i < visota - 1) and (0 < b < dlina - 1):
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()

# print("Первая задачка")
# nachalo = int(input("Введите начальный диапазон: "))
# final = int(input("Введите конечный диапазон: "))
# for a in range(nachalo, final + 1):
#     if a % 2 != 0:
#         print(a)

# print("Угадай число")
# num = int(input("Введите число от 1 и до 100: "))
# b = 54
# ch = 0
# # for a in range(num):
# while num != b:
#     if num < b:
#         print("Введите число больше")
#         num = int(input("Введите число от 1 и до 100: "))
#         ch += 1
#     if num > b:
#         print("Введите число меньше")
#         num = int(input("Введите число от 1 и до 100: "))
#         ch += 1
# else:
#     # num == b:
#     print("Вы угадали число")
#     print("Число попыток: ", ch)

# a = 2
# b = 15
# res = 0
# # if a > b:
# #     a, b = b, a
# a, b = ((a, b) if a < b else (b, a))
# while a <= b:
#     if a % 2:  # не приравнивает к нулю
#         res += a
#     a += 1
# print("Сумма: ", res)
# else:
#     while b <= a:
#         if b % 2:  # не приравнивает к нулю
#             res += b
#         b += 1
#     print("Сумма: ", res)


# a = [letter * 3 for letter in "Hello"]
# print(a)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)

#  Списки/Массив (list)
# num = [8, 3, "one", "independent", 1, 2, [2, 3, 3]]
# # print(type(num))
# # print(num[1])
# # print(num[5][0])
# # num[2] = 256
# # print(num)
# # num[1] += 100
# # num[3] += " most"
# # num[7] = 4
# # print(num)
#
# print("Длина списка: ", len(num))

# s = []
# print(type(s))
# b = list("Hello")
# print(b)

# s = [5] * 6
# print(s)

# n = list(range(2, 10, 2))
# print(n)
# n2 = [2, 4, 6, 8]
# print(n2)
#
# if n == n2:
#     print("Списки одинаковы")
# else:
#     print("Спики разные!")

# [выражение for переменная in последовательность]

# n = 5
# a = [i ** 2 for i in range(1, n+1)]
# print(a)

# a = [1, 2, 3]
# b = [5, 6]
# c = a + b
# print(c)
# d = c * 2
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# for i in range(len(a)):
#     a[i] = int(input("--> "))
#     print(a)
#

# a = [input("Введите индекс: ") for i in range(int(input("Введите значение: ")))]
# print(a)

# a = [4, 8, 3, 2, 3]
# for i in range(len(a)): # в i попадают индексы
# #   print(i)
#     print(a[i], end=" ")
# print()
# for elem in a:  # в elem попадают элементы
#     print(elem, end=" ")

# lst = ['один', 'два', 'три']
# for elem in lst:
#     print(elem * 2, end=" ")
# print()
# for i in range(len(lst)):
#     print(lst[i] * 2, end=" ")

# res = 0
# num = [0] * int(input("Введите значение: "))
# for elem in range(len(num)):
#     num[elem] = int(input("Введите индекс: "))
#     if num[elem] < 0:
#         res += num[elem]
# print("Сумма отрицательных элементов: ", res)


# a = [int(input("Введите индекс: ")) for i in range(int(input("n: ")))]
# res = 0
# for i in a:
#     res += i if i < 0 else 0
# print(res)

# a = [int(input("Введите индекс: ")) for i in range(int(input("n: ")))]
# count = 0
# for i in a:
#     if i < 0:
#         count += i
# print(count)

# lst = [int(input("Введите элементы: ")) for num in range(int(input("Введите числовой список: ")))]
# summa = 0
# for i in lst:
#     if i % 2:
#         summa += i
#     if i % 2 == 0:
#         i += 1
# print("Сумма нечетных элементов: ", summa)
# print("Количество четных элементов: ", i)

# n = list(range(21, 41))
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Количество четных чисел: ", k)
# print("Сумма нечетных чисел: ", s)

# lst = [int(input("Введите элементы: ")) for i in range(int(input("Введите числовой список: ")))]
# summa = 0
# count = 0
# for i in lst:
#     summa = (summa + i)
#     count += 1 if i != 0 else 0
# print(summa/count)

# lst = [int(input("Введите элементы: ")) for i in range(int(input("Введите числовой список: ")))]
# # for i in range(len(lst)):
# #     if i % 2 == 0:
# #         print(lst[i], end=" ")
#
# for i in range(0, len(lst), 2):
#     print(lst[i], end=" ")

# a = [7, 8, 2, 1, 17]
# a[0], a[-1] = a[-1], a[0]
# print(a)

# lst = [int(input("Введите элементы: ")) for i in range(int(input("Введите числовой список: ")))]
# for i in range(len(lst) - 1):
#     if lst[i + 1] > lst[i]:
#         print(lst[i + 1], end=" ")


# size = int(input("Введите размер поля: "))
# symbol = int(input("Введите количество символов: "))
# for i in range(7):
#     for j in range(5):
#         for n in range(3):
#             for m in range(4):
#                 print(" " if (i+n) % 2 else "*", end=" ")
#         print()
#

# Срезы
# Список [start:stop:step]
# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[2:])
# print(s[-2:2:-1])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# # print(s[::-1])
# # print(s[::2])
# # print(s[1::2])
# # print(s[:1])
# # print(s[6:7]) # [-1:]
# # print(s[3:4])
# # print(s[-3:1:-1])
# # print(s[2:5])
#
# # s[1:3] = [0, 0, 0, 0]
# # print(s)
# # s[1:2] = [20]
# # print(s)
# # s[3] = 30
# # print(s)

# Методы списков

# s = [10, 20, 0, 4, 2, 1, 94, 45]
# print(s)
# s.append(99)  # Добавляет элемент в конец списка
# print(s)
# s.extend([9, 8, 7])  # Добавляет множество элементов в конец обычного списка
# print(s)
# s.extend('add')
# print(s)

# d = []
# for i in range(1, 11):
#     d.extend([i ** 2])
# print(d)

# s = [1, 4, 5, 2, 10, 30, 25]
# s.insert(1, 100)
# print(s)

# lst = []
# n = int(input("Введите количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # lst.append(x)
#     # lst.extend([x])
#     lst.insert(0, x)
# print(lst)

# lst = []
# # kol = 0
# num = int(input("Введите количество элементов списка: "))
# for n in range(num):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         print(n % 3)
#         lst.append(x)
#         # kol += 1
#     else:
#         print("Число", x, " на 3 не делится ")
# print(lst)

# a = [5, 3, 2, 8, 4, 2, 4, 8]
# b = [1, 3, 5, 8, 9, 1]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3, 4, 5, 66, 77]
# b = [11, 22, 33, 44, 55]
# c = []
# if len(a) < len(b):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range (3,5)
#         c.append(b[i])
# if len(a) > len(b):
#     for i in range(len(b)):
#         c.append(b[i])
#         c.append(a[i])
#     for i in range(len(b), len(a)):  # range (3,5)
#         c.append(a[i])
# print(c)

# s = [1, 20, 0, 5, 3, 95, 0, 40]
# # s[4:] = []
# # if 0 in s:
# # s.remove(0)  # Удаляет элемент по значению, первое совпадение
# print(s)
# s[2:4] = []
# print(s)
# last = s.pop()
# print(last)
# print(s)
# second = s.pop(-2)
# print(s)
# # s.clear()
# # del s[:]
# print(s)

# # num = []
# # m = [num.append(int(input(" --> "))) for i in range(int(input("Введите количество элементов: ")))]
# num = [(int(input(" --> "))) for i in range(int(input("Введите количество элементов: ")))]
# k = int(input("Введите индекс: "))
# del num[k]
# print(num)

# (Первое задание!)
# num = [int(input(" Элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
# print("Список: ", num)
# k = []
# for a in num:
#     if a > 0:
#         k.append(a)
# print("Положительные числа: ", k)

# (Второе задание!)
# num = [int(input(" Элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
# x = int(input("Введите число: "))
# # for i in range(len(num)):
# #     if x == num[i]:
# #         print("Это число есть в списке")
# #         break
# #     if x != num[i] and i != len(num) - 1:
# #         continue
# #     print("Нет в списке")
# #     break
# if x in num:
#     print("Число есть в списке!")
# else:
#     print("Числа нет в списке!")

# s = [1, 2, 3, 1, 6, 3, 5, 2, 7]
# num = s.count(2)  # Считает количество заданных значений в списке
# print(num)
#
# ind = s.index(3, 3)  # Возвращает положение первого индекса с заданного значения
# print(ind)

# a = [1, 2, 3]
# b = a
# s_copy = a.copy()  # возвращает копию списка
# print("a = ", a)
# print("b = ", b)
# print("s_copy = ", s_copy)
# a.append(20)
# b.append(4)
# s_copy.append(315)
# print("a = ", a)
# print("b = ", b)
# print("s_copy = ", s_copy)

# s = [1, 2, 3, 4, 8, 1, 4, 2, 9]
# s.reverse()
# print(s)
# s.sort()
# print(s)
# s.sort(reverse=True)
# print(s)
#
# s2 = ["Виталий", "Сергей", "Алексей", "Алекс"]
# s2.sort(key=len)
# print(s2)

# srt = sorted(s)
# print(srt)

#  Генерация случайных данных

# import random
# import random
# print(random.randint(0, 5))  # Диапазон случайного числа с 0 и по 5 (включительно)
# print(random.randrange(0, 10, 2))

# from random import randint, randrange
# from random import *

#
# print(randint(0, 5))  # Диапазон случайного числа с 0 и по 5 (включительно)
# print(randrange(0, 10, 2))
# print(round(uniform(.5, 25.5), 2))
#
# s = [55, 66, 77, 88, 99, 20, 30, 90, 55]
# print(choice(s))
# print(choices(s, k=5))
#
# shuffle(s)
# print(s)

# mas = [randint(0, 100) for i in range(10)]
# print(mas)

# lst = [1, 3, 6, 1, 8, 2]
# # lst = ["s", "a", "r"]
# print(len(lst))
# print(sum(lst))  # sum работает только с числовыми значениями
# print(min(lst))
# print(max(lst))


# from random import *
# s = [randint(0, 100) for i in range(10)]
# max_ = max(s)
# print(s)
# print(max_)
# s.remove(max_)
# s.insert(0, max_)
# print(s)

# num = [randint(-20, 20) for i in range(10)]
# print(num)
# num.sort(reverse=True)
# print(num)

# num = [randint(0, 100) for i in range(10)]
# print(num)
# min_ = min(num)
# print("Min: ", min_)
# index_ = num.index(min_)
# print("Index min: ", index_)
# num[:index_] = []
# print(num)

# x = list('1a2b3c4d5g6h')
# print(x)
# print('a' in x)
# print('e' in x)
# print()
# print('a' not in x)
# print('e' not in x)

# lst = []
# # if len(lst) == 0:
# print(bool(lst))
# if not lst:
#     print("Список пустой!")


# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# n3 = a + b
# print("Третий список: ", n3)
#
# n3 = []
# for i in range(len(a)):
#     if a[i] not in n3:
#         n3.append(a[i])
# for i in range(len(b)):
#     if b[i] not in n3:
#         n3.append(b[i])
# print("Элементы обоих списков без повторений: ", n3)
#
# n3 = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in n3:
#         n3.append(a[i])
# print("Элементы общие для двух списков: ", n3)
#
# n3 = [min(a), min(b), max(a), max(b)]
# print(n3)

# num = int(input("Введите размер списка: "))
# lst = []
# while len(lst) < num:
#     m = randint(0, num)
#     if m not in lst and m < num:
#         lst.append(m)
# print(lst)

# s = [randint(0, 100) for i in range(10)]
# print(s)
# print("Сумма чисел: ", sum(s))
# print()
# p = [randint(0, 100) for j in range(10)]
# print(p)
# p.sort(reverse=True)
# print("Обратный порядок чисел: ", p)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print(m[1][2])

# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# for row in m:
#     for b in row:
#         print(b, end="\t")
#     print()
# print()
#
# q = [[b**2 for b in row]for row in m]
#
# for row in q:
#     for b in row:
#         print(b, end="\t\t")
#     print()


# row = int(input("Введите высота списка: "))
# col = int(input("Введите ширина списка: "))
# m = [[0 for b in range(col)]for a in range(row)]
# for i in m:
#     for j in i:
#         print(j, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)
# from random import *
# w, h = 5, 4
# matrix = [[randint(1, 30) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for col in row:
#         print(col, end="\t")
#     print()

# w, h = 3, 4
# otr = 0
# matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for col in row:
#         print(col, end="\t")
#         if col < 0:
#             otr += 1
#     print()
# print("Количество отрицательных чисел: ", otr)


# w, h = 3, 4
# otr = 1
# matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for col in row:
#         if col > 0:
#             otr *= col
#         print(col, end="\t")
#     print()
# print("Произведение ненулевых элементов: ", otr)

# w, h = 6, 6
# matrix = [[randint(0, 10) for x in range(w)] for y in range(h)]
# print(matrix)
# for i in range(0, 2, 6):
#     print()
#     matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
# print(matrix)

# print(dir(math))
# num1 = math.sqrt(2)
# print(num1)
# num2 = math.ceil(3.2)
# print(num2)
# num3 = math.floor(3.8)
# print(num3)
# print(math.pi)
#
# radius = 2
# print('Площадь окружности с заданным радиусом: ', radius, "=>", math.pi * (radius**2))

# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности: ", round(2 * radius * math.pi, 2))
# import time

# second = time.time()
# # print("Количество секунд с начала эпохи: ", second)
# # localtime = time.ctime()
# # print(localtime)
# res = time.localtime(second)
# print(res)
# print(res.tm_year)
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(9494999944)))
#
# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(pause, "seconds.")

# test = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(test)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

# import locale
# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime("Сегодня: %B %d %Y"))

# def hello(name, world):
#     print("Hello,", name,"said: ", world)
#
#
# hello("Ирина", "Hi")
# hello("Иван", "Hello")

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# n = 7
# m = 8
# get_sum(n, m)

# def symbol(count, a, b):
#     # print((a + b)*5)
#     for i in range(count):
#         if i % 2 != 0:
#             print(a, end=" ")
#         else:
#             print(b, end=" ")
#
#
# symbol(9, "+", "-")
# print()
# symbol(7, "X", "0")

# def get_sum(a, b):
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(4, 6))


# def sum_razn(x, y):
#     if a > b:
#         return a - b
#     if a < b:
#         return a + b
#
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе  число: "))
# print("Результат: ", sum_razn(a, b))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 10))

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Надёжный пароль!")
# else:
#     print("Ненадёжный пароль!")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))

# def sym(a=20, b='-'):
#     return b * a
#
#
# print(sym())
# n = int(input("Введите количество символов: "))
# m = input("Введите символ: ")
# print(sym(n, m))


# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s

#
# print("Сумма четных цифр: ")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print()
# print("Сумма нечетных цифр: ")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name: ", name, "\nAge: ", age)
#
#
# display_info("Ира", 24)
# display_info(age=25, name="Влад")


# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(id(lt1) == id(lt2))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(id(lt1))

# s = "hello"
# print(id(s))
# s += "World"
# print(id(s))

# s = "Hello"
# print(id(s))
# s = s[1:-1]
# print(s)
# print(id(s))

# lt1 = [1, 2, 3]
# print(id(lt1))
# # lt1 = lt1[1:-1]
# lt1 = lt1 + [4,5]
# print(lt1)
# print(id(lt1))

#  Кортеж (tuple)
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 2, 3, 4, 5)
# print(type(a))
# print(a)
# a = 1, 2, 3, 4, 5
# print(type(a))
# print(a)
# # b = tuple()
# # print(type(b))
#
# c = tuple("Hello")
# print(c)

# t = (1,)
# print(t)
# print(type(t))

# b = tuple((1, 2, 3, 4, 5))
# print(b[3])
# print(b[1:3])
# print(id(b))
# print(id(b[2]))
# # b[1] = 3

# s = tuple(int(input("-> ")) for i in range(3))
# print(s)
# from random import *
# s = input("Строка: ")
# a = tuple(s)
# print(a)

# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# tpl = tuple(mas)
# print(tpl)
# print()
# print(tuple(randint(0, 100) for j in range(10)))

# tpl = tuple((2 ** i) for i in range(1, 13))
# print(tpl)

# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# # print(len(t3))
# # print(t3.count('l'))
# # print(t3.count('s'))
# # print(t3.index("l", 2, 9))
# for i in t3:
#     print(i, end="")


# def slicer(tup, elem):
#     start = None
#     final = None
#     for i, item in enumerate(tup):
#         if item == elem:
#             start = i
#             break
#     if start is not None:
#         for i in range(start + 1, len(tup)):
#             if tup[i] == elem:
#                 final = i
#     if start is not None and final is not None:
#         return tuple(tup[start:final + 1])
#     else:
#         return tuple()


# tuple1 = (1, 2, 3, 4, 5, 3, 6, 4)
# elem1 = 3
# res1 = slicer(tuple1, elem1)
# print(res1)


# lst = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# row = 0
# for row in lst:
#     for col in row:
#         print(col, end=" ")
#     print()
# print("----------------")
# i = 0
# for col in row:
#     for row in lst:
#         print(row[i], end="\t")
#     i += 1
#     print()

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first+1)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))

# tpl1 = ran(0,6)
# tpl2 = ran(-5, 0)
# print(tpl1)
# print(tpl2)
# c = tpl1 + tpl2
# print(c)
# print("Нуликов - ", c.count(0))

# t = (10, 11, [1, 2, 3],(4, 5, 6), ["Hello", "World"])
# print(t, id(t))
# t[-1][0] = 'new'
# t[4].append('Hi')
# print(t)

# def tt(lst):
#     m = []
#     for i in lst[::-1]:
#         if i not in m:
#             m.append(i)
#     return tuple(m)
#
#
# print(tt([1, 2, 3, 3, 2]))
# print(tt([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))

# t = [1, 2, 3]
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # Распаковка кортежа
# print(x, y, z)
#
#
# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married

# user = get_user()
# print(user)
# print(user[0])
# name1, age1, is_married1 = user
# print(name1)

# a = (1, 2, 3)
# print(a)
# lst = list(a)
# lst.append(4)
# print(lst)
# tpl = tuple(lst)
# print(tpl)

# countries = (
#     ('Германия', 80.2, (('Берлин', 3.3), ('Гамбург', 1.7))),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.6)))
# )
#
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана: ", countryName, ", Население страны = ", countryPopulation, "млн людей")
#     for city in cities:
#         # print(city)
#         cityName, cityPopulation = city
#         print("\tГород: ", cityName, ", Населенность города: ", cityPopulation, "млн людей")

# Множество (set)

# s = {'banana', 'apple', 'orange'}
# print(type(s))
# print(s)
# print(len(s))

# a = []
# print(type(a))
# a = set('hello')
# print(type(a))
# print(a)

# s = {x * x for x in range(10)}
# print(s)

# num = [1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6]
# num = set(num)
# print(num)
# num = list(num)/
# num = list(set(num))
# print(num)

# def to_set(elem):
#     return set(elem), len(set(elem))
#
#
# print(to_set('Я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# t = {'red', 'green', 'blue'}
# # print('green' in t)
#
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r }
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)

# kor = ('ab', 'abcd', 'cde', 'abc', 'def')
# print(tuple(kor))
# s = 'ab'
# for i in tuple(kor):
#     if s in i:
#         print("Yes")
#     else:
#         print("No element")

# l = []
# kor = tuple(input("Введите символы без пробелов: "))
# print(kor)
# for i in kor:
#     if i in l:
#         l = i.count(i)
#     print(l)

# a = {'Tom', 'Bob', 'Alex', 'Tomi'}
# a.add('Ann')
# print(a)
# a.remove('Tom')
# print(a)
# user = 'Tom'
# if user in a:
#     a.remove(user)
# print(a)
# a.discard('Tom')
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# print(c)
# a.update(b)
# print(a)
# c = a & b
# print(c)
# a & b
# print(a)
# c = a - b
# print(c)
# c = a ^ b
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print("Количество уникальных элементов -", len(s))
# print("Минимальное значение - ", min(s))
# print("Максимальное значение - ", max(s))

# p1 = "Hello"
# p2 = "How are you?"
# p = set(p1)
# pp = set(p2)
# s = p & pp
# print(s)

# s1 = "Python"
# s2 = "Programming language"
# s = set(s1) - set(s2)
# print(s)

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# only = drawing ^ music
# both = drawing & music
# drawing = drawing - both
# print('Одно хобби: ', only)
# print('Оба хобби: ', both)
# print(drawing)


# s = frozenset([1, 2, 3, 4, 5, 6, 4])
# print(s)
#
# a = frozenset(["hello", "world"])
# print(a)

#  Словари (dict)

# s = ["one", "two"]
# print(s[0])
# d = {1: 'one', 2: 'two'}
# print(d[1])

# c = {}
# print(c)
# print(type(c))

# c = dict(one=1, two=2)
# print(c)
# print(type(c))

# a = [
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('alex@gmail.com', 'Alex')
# ]
# d = dict(a)
# print(d)

# d = {a: a ** 2 for a in range(1, 7)}
# print(d)
# print(d[2])
# d[2] = 15
# print(d[2])

# d = {0: 'text', 'one': 45, (1, 2.3): 'кортеж', 42: [2, 3, 6, 7], True: 1}
# print(d)
# print(d[True])
# print(d[42][1])
# print('one' in d)
#
# print(d.keys())
# if 'one' in d:
#     print('True')
# key = (1, 2.3)
# # if key in d:
# #     del d[key]
# # print(d)
# try:
#     del d[key]
# except KeyError:
#     print("Значения нет в словаре" + str(key))

# for key in d:
#     print(key, '-->',  d[key])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
#
# pr = 1
# for i in d:
#     pr *= d[i]
# print(pr)

# d = dict()
# d[1] = input("Введите овощ: ")
# d[2] = input("Введите овощ: ")
# d[3] = input("Введите овощ: ")
# d[4] = input("Введите овощ: ")
# print(d)

# d = {i: input("Введите овощ: ") for i in range(1, 5)}
# print(d)
# a = int(input("Какой элемент исключить из списка? "))
# if a in d:
#     del d[a]
#     print(d)
# else:
#     print("Такого элемента нету!")

# capitals = dict()
# capitals['Молдова'] = 'Кишинев'
# capitals['Румыния'] = 'Бухарест'
# capitals['Россия'] = 'Москва'
#
# countries = ['Молдова', 'Румыния', 'Россия', 'Франция']
#
# for country in countries:
#     if country in capitals:
#         print('Столица страны ' + country + ': ' + capitals[country])
#     else:
#         print('Нету страны - ' + country)

# processor = {
#     '1': ['Core i3-4330', 9, 4500],
#     '2': ['Core i5-4760k', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400]
# }
# for item in processor:
#     print(item, ')', processor[item][0], ' - ', processor[item][1], ' штук по. ', processor[item][2], ' руб.', sep="")
# while True:
#     n = input("Номер: ")
#     if n != '0':
#         cnt = int(input("Добавить Количество: "))
#         processor[n][1] = cnt + processor[n][1]
#     else:
#         break
#
# for item in processor:
#     print(item, ')', processor[item][0], ' - ', processor[item][1], ' штук по. ', processor[item][2], ' руб.', sep="")

# users = ["John", "Tom", "Anne", "Fiona"]
# Regions = [
#     {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# ]
# for user in users:
#     print(user)
#     for region in Regions:
#         print(region)
# while True:
#     n = input("Что хотите изменить? ")
#     if n == Regions:
#

# d = {'a': 1, 'b': 2, 'c': 3}
# # print(d['b'])
# # value = d.get('e', 'False')
# # print(value)
# # print(d)
# # # item = d.items()
# # # print(item)
# # # key = d.keys()
# # # print(key)
# # # value = d.values()
# # # print(value)
# # #
# # # for i, j in d.items():
# # #     print(i, '->', j)
# # # d.clear()
# # # pop = d.pop('b')
# # # print(pop)
# # # it = d.popitem()
# # # print(it)
# # # item = d.setdefault('e', 5)
# # # print(item)
# # update = d.update({'a': 7, 'q': 9})     # [('r', 7), ('q', 9), ('a', 11)]
# # print(update)
# # print(d)
# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
# d['e'] = 7
# d2['b'] = 5
# print()
# print("D =", d)
# print("D2 =", d2)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)

# info = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'NewYork'}
# NewInfo = info.copy()
# NewInfo.pop('age')
# NewInfo.pop('city')
# print(info)
# print(NewInfo)

# info = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'NewYork'}
# # NewInfo['name'] = info.pop('name')
# # NewInfo['salary'] = info.pop('salary')
# # print(info)
# # print(NewInfo)
# info['location'] = info.pop('city')
# print(info)
# info.setdefault('pets', 'kity')
# print(info)

# a = {
#     'First': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'Second': {
#         4: 'four',
#         5: 'fife'
#     }
# }

# print(a)
# for i in a:
#     print(i)
#     for o in a[i]:
#         print('\t', o, ": ", a[i][o], sep="")

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# a = {key: value for key, value in d.items() if value <= 2}
# print(a)
# a = {i: i * 5 for i in [10, 20, 30, 40]}
# print(a)
# a = {i: i * 5 for i in 'Hello'}
# print(a)
# value = int(input("-> "))
# lt = [1, 2, 3, 4, 5]
# a = {i: value for i in lt}
# print(a)
# d = dict.fromkeys(['a', 'b'], 100)
# print(d)
# value = int(input("-> "))
# # lt = [1, 2, 3, 4, 5]
# a = {i: value for i in range(1, 9)}
# print(a)

###### list()
# figures = {1: 'Rectangle', 2: 'Triangle', 3: 'Circle'}
# # value = list(figures.values())
# # value = list(figures.keys())
# value = list(figures.items())
# print(value)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = {}
# s = None
# for elem in a:
#     if type(elem) == str:
#         d[elem] = []
#         s = elem
#     else:
#         d[s].append(elem)
# print(d)
# zip()
# d = list(zip([12, 1, 2], ['Dec', 'Jan', 'Feb']))
# d = dict(zip([12, 1, 2], ['Dec', 'Jan', 'Feb']))
# print(d)

# a = [12, 1, 2]
# b = ['Dec', 'Jan', 'Feb']
# f = {k: v for k, v in zip(a, b)}
# print(f)
# a = [1, 2, 3]
# b = [5]
# print(list(zip(a, b)))
# print(list(zip(range(5), range(100))))

# a = {'name': 'Igor', 'last_name': 'Doe', 'Job': 'Consultant'}
# b = {'name': 'Alex', 'last_name': 'Seo', 'Job': 'Driver'}
#
# # for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
# for (k1, v1), v2 in zip(a.items(), b.values()):
#     print(k1, '-> ', v1, ",", v2)
#     # print(k2, '-> ', v2)
# a = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# x, y = zip(*a)
# print(x)
# print(y)
# lt1 = [2, 1, 4, 3]
# lt2 = ['a', 'b', 'c', 'd']
# # a = list(zip(lt1, lt2))
# # print(a)
# # a.sort()
# a1 = sorted(zip(lt1, lt2))
# print(a1)
# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000.00]
# production_cost = [46800.00, 45900.00, 43200.00]
#
# for m, sales, cost in zip(month, total_sales, production_cost):
#     res = sales - cost
#     print("Чистая прибыль в", m, "->", res)
# one = {'apple': 0.4, 'orange': 0.35, 'banana': 0.6}
# two = {'peper': 0.2, 'onion': 0.55}
# print({**one, **two})
#
# for k, v in {**one, **two}.items():
#     print(k, "->", v)
# num = int(input("Введите количество студентов: "))
# stud = {}
# s = 0
# for i in range(num):
#     s_name = input(str(i+1) + "й студент -> ")
#     point = int(input("Балл -> "))
#     stud[s_name] = point
#     s += point
# average = s/num
# print("Средний балл: ", round(average, 1))
# print("Студенты с баллом выше среднего -> ", )
# for i in stud:
#     if stud[i] > average:
#         print(i)
# en = ['red', 'green', 'blue']
# j = 1
# for i in en:
#     print(j, "-й цвет -> ", i, sep="")
#     j += 1

# en = ['red', 'green', 'blue']
# for j, i in enumerate(en, 1):
#     print(j, "-й цвет -> ", i, sep="")
#     j += 1
# en = {0: 1, 1: 2, 2: 3}
# for i, j in enumerate(en):
#     print(i, ": ", j, " -> ", en[j], sep="")
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, 4, 'abs'))
# print(func())
# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# num1 = summa(1, 2, 3, 4, 5, 6, 7, 8)
# num2 = summa(6, 7, 8)
# print(num1)
# print(num2)
# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))
# def summa(*args):
# summ = 0
# average = 0
# for i in args:
#     summ += i
#     average = summ/i
# for b in args:
#     if average > b:
#         print(b)
# return average

#     lst = []
#     a = sum(args)/len(args)
#     print(a)
#     for i in args:
#         if i < a:
#             lst.append(i)
#     return lst
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(3, 6, 1, 9, 5))
# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 4, 2, 4, 'abc'))
# def print_scores(stud, *scores):
#     print("Student name: ", stud)
#     for score in scores:
#         print(score, end=" ")
#     print()
#
# print_scores('Alex', 100, 95, 94, 80, 58)
# print_scores('John', 45, 85, 15, 25, 33)
# def nums(*args):
#     res = []
#     for i in args:
#         res.append(int(str(i)[::-1]))
#     return res
#
#
# print(nums(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# # print(nums(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, 'only_odd=True'))
# def reverse(n):
#     # s = str(n)
#     return int(str(n)[::-1])
#
#
# def nums(*args, only_odd=False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2):  # True or False(Первая часть) / # False or True(Вторая часть)
#             res.append(reverse(i))
#     return res
#
#
# print(nums(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(nums(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))
# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a="Python"))
# def info(**employer):
#     for k, v in employer.items():
#         print(k, '->', v)
#     print('*' * 20)
#
#
# info(first_name='Irina', last_name='Petrova', age=25, Number= +384272888)
# info(first_name='Alex', last_name='Sivio', age=30, Number= +3822727488, email='Sivio@gmail.com',location='Moldova')
# def info(**infos):
#     my_dict.update(infos)
#
#
# my_dict = {'one': 'first'}
# info(k1=22, k2=31, k3=11, k4=91)
# info(name='Bob', age=31, weight=61, eyes_color='gray')
# print('my_dict =', my_dict)
# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1, 2, 3, 4, 5)
# func2(one=123, two=456)
# def func(a, *args, one=True, **kwargs):
#     return a, args, kwargs, one
#
#
# print(func(5, 9, 6, 3, one=False, b=2, c=3, d=4))
################ Область видимости (scope)

# name = "Tom"


# def hi():
#     print('Hello', name)
#
#
# def bye():
#     global name
#     name = 'Bob'
#     print("By", name)
#
#
# hi()
# bye()
# print(name)
# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()
# def add_two(a):
#     x = 2
#     return a + x
#

# print(add_two(3))

# x = 3
# def func(a):
#     x = 2
#
#     def inner():
#         x = 4
#         return x
#
#     return inner()

# print(func(4))
# a = [1, 2, 3, 4, 5]
# print(max(a))
# import builtins
# print(dir(builtins))

# def proiz(*mem):
#     pr = 1
#     for i in mem:
#         pr *= i
#     return pr
#
# print(proiz(10, 9))
# print(proiz(2, 3, 4))
# print(proiz(3, 5, 10, 6))
####################################### Вложенные функции

# def outer_func(who):
#     def inner_func():
#         print("Hello", who)
#     inner_func()
#
#
# outer_func("world")
# def func1():  # 2
#     a = 6
#
#     def func2(b):  # 5
#         a = 4
#         print("Сумма ", a + b)  # 6
#
#     print("a = ", a)  # 3
#     func2(5)  # 4
# func1()  # 1
# x = 25


# def fn():
#     global t
#     a = 30
#     t = a
#     print("global: ", x)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal: ", a)
#
#     inner()
#     t = a
#
#
# fn()
# z = x + t
# print('Result ', z)
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x = ", x)
#
#     fn2()
#     print('fn1.x= ', x)
#
# fn1()
# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)
# def increment(num):
#     def inner():
#         return num + 1
#
#     return inner()
#
#
# res = (increment(3))
# print(res)


# #################################### Замыкание
# def outer(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# print(outer(5)(10))

# res = outer(5)
# print(res(10))
# print(res(2))
#
# res2 = outer(7)
# print(res2(5))
# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         c.append(4)
#         nonlocal a, b
#         a = a + 1
#         b = b + ' new'
#         return a, b, c
#
#     return func2


# func = func1()
# print(func())

# def outer(town):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(town , s)
#     return inner
#
#
# res1 = outer('Кишинев')
# res1()
# res1()
# res2 = outer('Одесса')
# res2()
# res2()
# res2()
# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Elise': 79,
#     'Fiona': 35,
#     'Grace': 69
# }


###################def make_classifier(lower, upper):
#     def classifier_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return classifier_student
#
#
# A = make_classifier(80, 101)
# B = make_classifier(70, 80)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
# print(A(students))
# print(B(students))
# print(C(students))
# print(D(students))
# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())
# s = 0
#
#
# def outer(a, b, c):
#     def inner(x, y):
#         global s
#         s = x * y
#         return s
#
#     return 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#
#
# print(outer(5, 2, 3))
# print(outer(1, 2, 3))
############################# Анонимные функции и lambda выражения
# print((lambda x, y: x + y)(1, 2))
# print('res = ', (lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'a'))
# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
# print(summ())
# print(summ(10, 20))
# func1 = lambda *args: args
# print(func1(1, 2, 3, 4))
# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
# for t in c:
#     print(t("abc_"))
# def inc(n):
#     return lambda x: x + n
#
# f = inc(42)
# print(f(3))


# def inc1(n):
#     def wrap(x):
#         return x + n
#     return wrap
#
# f1 = inc(42)
# print(f1(3))
#
# inc2 = (lambda n: (lambda x: x + n))
# # f2 = inc2(42)
# # print(f2(3))
# print(inc2(42)(3))
# print((lambda n: (lambda x: x + n))(42)(3))

# print("Сумма чисел: ", (lambda n: (lambda x: (lambda m: n + x + m)))(2)(4)(6))
# d = {'b': 15, 'a': 10,  'c': 4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# dict1 = dict(lst)
# print(dict1)
# players = [{'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}]
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# # players.sort(key=lambda item: item['last name'])
# # print(players)
# players.sort(key=lambda item: item['raiting'])
# print(players)
# players.sort(key=lambda item: item['raiting'], reverse=True)
# print(players)
# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[3](12, 5)
# print(b)
# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))
# d = {
#     1: (lambda: print("Понедельник")),
#     2: (lambda: print("Вторник")),
#     3: (lambda: print("Среда")),
#     4: (lambda: print("Четверг")),
#     5: (lambda: print("Пятница")),
#     6: (lambda: print("Суббота")),
#     7: (lambda: print("Воскресенье"))
# }
#
# d[4]()
# minimum = (lambda a, b, c: a if a < b else b if b < c else c)
# print(minimum(24, 11, 10))
# Функция - map()
# def mult(t):
#     return t * 2


# lst = [2, 8, 12, -5, 10]
# # print(list(map(mult, lst)))
# print(list(map(lambda t: t * 2, lst)))
# t = 2.88, -1.75, 100.55
# print(list(map(lambda x: str(x), t)))
#
# a = ['2.88', '-1.75', '100.55']
# print(list(map(float, a)))
# areas = [3.576845, 5.923829, 7.195837, 56.827491, 9.823461, 32.142954]
# print(list(map(round, areas, range(1, 7))))
# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# lst = list(map(lambda x, y: (x, y), st, num))
# print(lst)
# tp = dict(lst)
# print(tp)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# lst = list(map(lambda x, y: (x + y), l1, l2))
# print(lst)

# Первое задание!
# a = (lambda x, y, z: x * y * z)
# b = a(2, 5, 5)
# print(b)
# Второе задание!
# l1 = [
#     {'name': 'Jeniffer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
#
# l1.sort(key=lambda item: item['name'])
# l1.sort(key=lambda item: item['final'], reverse=True)
# print(l1)
# Третье задание
# l1 = {'name': 'Jeniffer', 'final': 95},
#      {'name': 'David', 'final': 92},
#      {'name': 'Nikolas', 'final': 98}
#
# def points(lower, upper):
#     def people(info):
#         return {k: v for k, v in info.items() if lower <= v < upper}
#     return people
#
#
# a = points(98, 95)
# print(a(l1))
#################### filter (function(), цикл)
# t = ('abcd', 'abc', 'ab', 'cdeftd', 'de', 'gfe', 'ple')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
# b = [66, 76, 90, 84, 32, 45, 91, 99]
# res = list(filter(lambda s: 75 < s < 88, b))
# print(res)
# from random import *
# s = [randint(0, 30) for i in range(10)]
# print(s)
# res = list(filter(lambda m: 10 < m < 21, s))
# print(res)

# s = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda m: m % 15 == 0, s))
# print(res)
############### Декораторы
# def hello():
#     return 'Hello, i am func "hello"'
#
#
# def super_func(func):
#     print('Hello, i am func "super_func"')
#     print(func())
#
#
# super_func(hello)
#
# test = hello
# print(test())
# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# def func_test():
#     print('Hello, i am func!')
#
#
# test = my_decorator(func_test)
# test()
# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return wrap
#
#
# @my_decorator  # Декоратор
# def func_test():  # Декорируемая функция
#     print('Hello, i am func!')
#
# @my_decorator
# def my_name():
#     print('Твой черный день!')
#
#
# func_test()
# print()
# my_name()
# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</br>'
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<a>' + fn() + '</a>'
#     return wrap
#
#
# @bold
# def hello():
#     return 'text'
#
#
# @italic
# def mine():
#     return 'Tuk tuk'
#
#
# print(hello())
# print(mine())
# def one1(word):
#     count = 0
#
#     def one_1():
#         nonlocal count
#         count += 1
#         word()
#         print("Вызов функции: ", count)
#     return one_1
#

# @one1
# def hello():
#     print("Hello")
#
# @one1
# def bye():
#     print("Bye mate")
#
#
# hello(), bye()
# hello(), bye()
# hello(), bye()
#
# def srgs_decorator(fn):
#     def wrap(arg1, arg2):
#         print("*" * 50)
#         fn(arg1, arg2)
#         print("*" * 50)
#     return wrap
#
# @srgs_decorator
# def print_fullname(firstname, lastname):
#     print("Меня зовут: ", firstname, lastname)

# def srgs_decorator(fn):
#     def wrap(*args, **kwargs):
#         fn(*args, **kwargs)
#         print("*" * 50)
#         print('args', args)
#         print('kwargs', kwargs)
#         print("*" * 50)
#     return wrap
#
#
# @srgs_decorator
# def print_fullname(a, b, c, study='Python'):
#     print(a, b, c, 'Изучают', study)
#
#
# print_fullname('Alexandru', 'Dezmond', 'Lucius', study='JavaScript')
# print()
# print_fullname('Jenya', 'Alina', 'Ann')
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
# @decor("Сложение:", "+")
# def summa(a, b):
#     print(a + b) \
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
# summa(5, 2)
# sub(5, 2)

# def decor(fn):
#     def wrap(x):
#         def inner_wrap(num):
#             return 'Результат: ' + str(x(num) * fn)
#         return inner_wrap
#     return wrap
#
# @decor(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))
# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Несоответствует тип данных!")
#             for j in kwargs:
#                 if type(f_kwargs[j]) != kwargs[j]:
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args, **f_kwargs)
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z='Hello'):
#     return (x + y) * z


# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# print(typed_fn2("Hello,", "World", "!"))
# print(typed_fn3("Hello,", "World,", z=5))
# def avr(fn):
#     def wrap(*args):
#         print(args)
#         print(*args)
#         a = ''
#         for i in args:
#             a += str(i) + ", "
#         print("Среднее арифметическое: ", a[:-2], "=", fn(*args) / len(args))
#     return wrap
#
# @avr
# def summer(*ar):
#     print("Сумма чисел: ", *ar, "=", sum(ar))
#     return sum(ar)
#
#
# summer(2, 3, 4, 4)
# def decor(tx=None, decor_text=''):
#     def wrapper(fn):
#         def wrap(*args):
#             print(decor_text, end="")
#             fn(*args)
#
#         return wrap
#
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#
# @decor
# def hello_world2(text):
#     print(text)
#
#
# @decor(decor_text="Hello, ")
# def hello_world(text):
#     print(text)


# hello_world2('Hi')
# hello_world('World!')
# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 7))
# print(bin(18)) # 0b10010 # 0B - Двоичная система счисления
# print(oct(18)) # 0o22    # 0o
# print(hex(18)) # 0x12    # 0x
# q = 'Pyt'
# w = 'hon'
# s = q + w
# print(s)
# # # print(s * 2)
# # # print('y'in q)
# # print(s[-1::-1])
# s = s[:3] + 't' + s[4:]
# print(s)
# a = 'Я изучаю Nuthon.'
# b = ' Мне нравится Nuthon.'
# c = ' Nuthon очень интересный язык программирования.'
# d = a + b + c
# print(d)
# a = a[:9] + 'P' + a[10:]
# b = b[:14] + 'P' + b[15:]
# c = c[:1] + 'P' + c[2:]
# d = a + b + c
# print(d)

# def change_char(s, c_old, c_new):
#     s2 = ""
#     for i in s:
#         if i == c_old:
#             s2 += c_new
#         else:
#             s2 += i
#     return s2

# def change_char(s, c_old, c_new):
#     s2 = ""
#     for i in s:
#         if c_old not in i:
#             s2 += i
#         else:
#             s2 += c_new
#     return s2
#
#
# st = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования.'
# st2 = change_char(st, 'N', 'P')
# print('st1 =', st)
# print('st2 =', st2)
# print(u"Привет")
# print(r"C:\file.txt") # Сырые строки
# print(r"C:\file.txt\\"[:-1])
# print(r"C:\file.txt" + "\\")
# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне исполнилось " + str(age) + " лет")
# print("Меня зовут ", name, ". Мне исполнилось ", age, " лет", sep="")
# print(f"Меня зовут {name}. Мне исполнилось {age} лет")
#
# print(f"{round(2.355363, 2)}")
# print(f"{2.355363:.2f}")
# x = 10
# y = 5
# print(f"({x} * {y}) / 2 = {int(x * y / 2)}"
#       f" - выражение")
# d = 74
# print(f"{{{{{{{{{{{d}}}}}}}}}}}")
# dir_name = 'doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# s = """<div>
#     <a href="#">content</a>
# </div>
# """
# print(s)
# s1 = '''<div>
#     <a href="#">content</a>
# </div>
# '''
# print(s1)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# import math
#
#
# def cylinder(r, h):
#     """
#     Функция вычисляет площадь цилиндра.
#
#     Функция вычисляет площадь цилиндра на основании, заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# while True:
#     b = (int(input("Введите число: ")))
#     if b > 0:
#         a = bin(b)
#         print(a)
#     else:
#         print("Отрицательное число!")
#         break
# print(ord('a'))
# while True:
#     n = input("-> ")
#     if n != '-1':
#         print(ord(n))
#     else:
#         break
# my_str = 'Test string for me'
# arr = [ord(x) for x in my_str]
# print(arr)
# summa = [int(sum(arr) / len(arr))] + arr
# print(summa)
# summa += [x for x in [ord(x) for x in (input('-> '))[0:3]] if x not in summa]
# print(summa)
# if summa[-1] in summa[:-1]:
#     print(summa.count(summa[-1]) - 1)
# summa.sort(reverse=True)
# print(summa)
# print(chr(97))
# print(chr(35))

# a = 122
# b = 97
# while b <= a:
#     print(chr(b), end=" ")
#     b += 1
#
# print('apple' == 'Apple')
# print('Apple' < 'appLe')
# print(ord('a')) # 97
# print(ord('A')) # 65
# from random import randint
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_pass():
#     random_length = randint(SHORTEST, LONGEST)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print('Ваш случайный пароль: ', random_pass())
# print(dir(str))
# s = 'hello, WORLD! I am learning Python.'
# # print(s.capitalize())
# # print(s.lower())
# # print(s.upper())
# # print(s.swapcase())
# # print(s.title())
# #
# # print(s.count("l", 3))  # Подсчитывает количество вхождений подстроки в строку
# # print(s.find("Python1")) # Ищет в строке заданную подстроку, если она найдена, возвращает индекс подстроки, если не
# # # найдена, возвращает значение -1
#
# # a = 'один два'
# # b = a[:a.find(" ")]
# # c = a[a.find(" ")+1:]
# # print(b)
# # print(c)
# # print(c + " " + b)
#
# # s = 'ab12c59p7dq'
# # digits = []
# # for i in s:
# #     if i in '1234567890':
# #         digits.append(i)
# # print(digits, end=" ")
#
# # s = 'ab12c59p7dq'
# # digits = []
# # for i in s:
# #     if '1234567890'.find(i) >= 0:
# #         digits.append(i)
# # print(digits, end=" ")
# print(s)
# # print(s.index("Python"))
# p = s.rfind('l')
# print(s.rindex('n'))
#
# s = 'I am learning Python. hello, WORLD!'
# # first = s.find('h')
# # second = s.rfind('h') + 1
# # new_s = (s[:first] + s[second:])
# new_s = (s[:s.find('h')] + s[s.rfind('h') + 1:])
# print(new_s)
# print('abc123'.isalnum())
# print('ABCabc'.isalpha()) # Определяет состоит ли строка из букв
# print('1212'.isdigit()) # Определяет состоит ли строка из цифр
# print('abc'.islower()) # Определяет состоит ли строка из строчных букв
# print('abc'.isupper()) # Определяет состоит ли строка из букв верхнего регистра

# print('py'.center(100, '-')) # Выравнивание строки по центру
# print("    py".lstrip())
# print("py    ".rstrip())
# print("    py   ".strip())
#
# print('https://www.python.org'.lstrip('/:pths')) # Удаляет элементы в параметрах
# print('py.$$$;'.rstrip('$;.'))
#
# print('https://www.python.org'.lstrip('tpsh/:w').rstrip('rog.'))
# s = '11 23 44 55 23 22'
# s_old = input('Заменяемая подстрока: ') # 23
# s_new = input('Новая подстрока: ') # !!
# i = s.find(s_old) # индекс - 3
# while i != -1:
#     l = len(s_old) # 2(количество символов)
#     s = s[0:i] + s_new + s[i+l:]  # 11 + !!! +
#     i = s.find(s_old)  # 13
# print(s)
# st = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования.'
# print(st)
# print(st.replace('Nython', "new", 2))  # Заменяет слова или строки
# s = "*"
# seq = ('a', 'b', 'c')
# print(s.join(seq))  # a-b-c
#
# print("..".join(['1', '2'])) # Метод join объединяет итерируемую последовательность (список, кортеж, другая строка)
# # в строку
# print(":".join("Hello"))
# print("Строка разделенная пробелами".split()) # Делит строку на список из подстрок
# # print("Строка_разделенная_про_белами".split("_"))
# # print("Строка разделенная пробелами".split("а"))
#
# print('www.python.org'.split(".", 1))
# a = list(map(int, input("-> ").split()))
# print(a)

# info = input("Введите ФИО: ").split()
# print(info[0], " ", info[1][0], ".", info[2][0], ".", sep="")
# print('www.python.org.ru'.rsplit(".", 2))
# print('www...python...org'.split('.'))
# print('www...python...org'.split('...'))

#######Вариант 1##################
# sym = "*"
# s = 'В строке заменить пробелы символом'
# print(s.split())
# print(f"В{sym}строке{sym}заменить{sym}пробелы{sym}символом{sym}")

########Вариант 2################
# s = 'В строке заменить пробелы символом'.split()
# print("*".join(s))
# import re
# ################################### Регулярные выражения ##################################
# s = "Я ищу 5 совпадения в 2023 году. И я их найду в 2 счёта. 9238231"
# # # reg = '[12][09][0-9][0-9]'  # Возвращает любой из найденных последовательностей
# # reg = '[А-яё.]'
# reg = r'\d'
# # # # print(s.find(reg))
# # # # print(re.findall(reg, s))  # Вовзращает список, содержащий все совпадения
# # # # print(re.findall("2", s))
# # # print(re.search(reg, s).span())
# # # print(re.search(reg, s).start())
# # # print(re.search(reg, s).end())
# # # print(re.search(reg, s).group())
# # # print(re.match(reg, s))  # Поиск по заданному шаблону в начале строки
# # # print(re.split(reg, s))  # возвращает список, в котором строка разбита по шаблону
# # # print(re.sub(reg, "!", s))  # Заменяет совпадение, указанным текстом
# # print(re.findall(reg, s))
# # s1 = "Ели[-ели]."
# # pattern = r"[А-яё.\[\]-]"
# # print(re.findall(pattern, s1))
# # s = 'Час в 24-часовом формате от от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09.'
# # pattern = '[0-2][0-9]:[0-5][0-9]'
# # print(re.findall(pattern, s))
# print(re.findall(reg, s))
import re
# # i = input("Введите строку: ")
# # print(re.sub("о", "О", i))
# # s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9578 19_4 5"
# # reg = r'\w'
# #
# #
# # print(re.findall(reg, s))
# # s1 = 'Цифры: 7, +17, -42, 0013, 0.3'
# # # pattern = r'[+-]?\d+\.?\d*'
# # print(re.findall(pattern, s1))
# #
# # s1 = '05-03-1987 # Дата рождения'
# #
# # new = (re.sub(r'#.*', '', s1))
# # print('Дата рождения:', re.sub(r'-', '.', new))
# #
# # # Дата рождения: 05.03.1987
# # s1 = 'author=Пушкин А. С. ; title = Евгений Онегин; price =200; year= 1831 '
# # pattern = r'\w+\s*=[^;]+'
# # print(re.findall(pattern, s1))
# # s1 = '12 сентября 2023 года '
# # reg1 = r'\d{2,4}'
# # print(re.findall(reg1, s1))
# # num = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# # # reg = r'\d{11}'
# # reg = r'\+?\d{11}'
# # print(re.findall(reg, num))
# # s = "Я ищу совпадения в 2023 году. И я их найду в 2000000000 счёта. 9578 19_4 5"
# # # reg = r'^\w+\s\w+'
# # reg = r'\w+\s\w+$'
# # print(re.findall(reg, s))
#
# #
# # def login(a):
# #     return re.findall(r'^[\w!@#$-]{8,16}$', a)
# #
# #
# # print(login("admin_admin"))
# # print(login("!admin_admin$$"))
# # print(re.findall(r"\w+", '12 + м'))
# # print(re.findall(r"\w+", '12 + м', flags=re.ASCII))
# # print(re.findall(r'[а-я]', 'Я я', re.IGNORECASE))
# # text = """
# # one
# # two
# # """
# # print(re.findall(r'one$', text))
# # print(re.findall(r'one$', text, re.MULTILINE))
# # text = """
# # one
# # two
# # """
# # print(re.findall(r'one.\w+', text))
# # print(re.findall(r'one.\w+', text, re.DOTALL))
# #
# # def password(a):
# #     return re.findall(r"^[\w+-@0]{8,16}$", a)
# #
# #
# # print(password('my-p@ssw0rd'))
# # adressa = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
# # reg = r"[\d\w@_.-]+"
# # print(re.findall(reg, adressa))
#
# # test = 'Python (в русском языке встречатются названия питон[16] или пайтон [17]) - высокоуровневый язык
# # программирования общего назначания с динамической строгой типизацией и автоматическим управлением памятью [18][19]'
# # reg = r'\d{2}'
# # print(re.findall(reg, test))
#
# # info = input("Введите дату в формате dd-mm-YY: ")
# # reg = r'\d{2,4}'
# # print(re.findall(reg, info))
# # def func(num):
# #     a = r'(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
# #     return bool(re.match(a, num))
# #
# #
# # print(func('MMDCCLXXIII'))
# # print(func('CCCMMVIIVV'))
# # print(re.findall("""
# # [A-z.-]+   # part 1
# # @          # поиск символа @
# # [a-z_.-]+  # part 2
# # """, 'test@mail.ru', re.VERBOSE))
# # text = 'hello world'
# # print(re.findall(r'\w+', text, re.DEBUG))
# # text = """Python,
# # python,
# # PYTHON"""
# # reg = '(?im)^python'
# # print(re.findall(reg, text))  # flags=re.IGNORECASE | re.MULTILINE
# # s = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
# # reg = r'[\w.-]+@[\w.]+[^., ]'
# # print(re.findall(reg, s))
# # text = '<body>Пример жадного соответствия регулярных выражений</body> '
# # print(re. findall('<.+?>', text))
# # greedy (жадный квантификатор)
# # lazy (ленивый  квантификатор)
#
# # *?, +?, ??
# # {m,n}?, {,n}?, {m,}?
#
# # t = '2342 78 22 999'
# # reg = '\d{1,3}?'  # Берет минимум , по одной цифре
# # print(re. findall(reg, t))
# # s = '<p>Изображение <img alt="картинка" src= "bg.jpg"> - фон страницы</p>'
# # reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# # print(re. findall(reg, s)) # <img src= "bg.jpg">
#
# # test = '''Python (в русском языке встречаются названия питон[16] или пайтон [17]) - высокоуровневый язык
# # программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью [18][19]'''
# # reg = r'\[\d+]'
# # print(re.findall(reg, test))
# # s = 'Петр и Ольга отлично учатся'
# # reg = 'Петр|Виталий|Ольга'
# # print(re.findall(reg, s))
# # s = 'int = 4, float = 4.0, double = 8.0f'
# # # reg = r'int\s*=\s*\d[.\w+]*|float\s*=\s*\d[.\w+]*|double\s*=\s*\d[.\w+]*'
# # reg = r'(?:int|float|double)\s*=\s*\d[.\w+]*'
# # print(re.findall(reg, s))
#
# # () - группирующая скобка
# # (?:) - группирующая скобка, не сохраняющая
# # # 192.168.255
# # s = '127.0.0.1'
# # # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# # reg = r'(?:\d{1,3}.){3}\d{1,3}'
# # print(re.findall(reg, s))
# # s = 'Word2016, PS6, AI5, '
# # reg = r'(([A-z]+)(\d*))'
# # print(re.findall(reg, s))
# # s = "5 + 7 * 2 -4"
# # # reg = r'\s*[+*-]\s*' # ['5', '7', '2', '4']
# # reg = r'\s*([+*-])\s*' # ['5', '+', '7', '*', '2', '-', '4']
# # print(re.split(reg, s))
#
# s = '24-24-2004'
# reg = r'\d+\d+\d+'
# print(re.findall(reg, s))

# p = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, p).group())
# m = re.search(reg, p)
# print(m[1])
# print(m[2])
# print(m[0])

# num = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# reg = r'[+]*7\s*499\s*(?:\d+[-]*){3}'
# print(re.findall(reg, num))
print("Hello")
