################ Пишется в регулярных выражениях ##################
####### Наименование группы регулярного выражения
# (?P<q>) - дать имя круглой скобке, в угловых скобках - само имя.
# (?P=q) - Обращение к скобке

# pattern - Шаблон
# repl - на что заменяем
# string - строка, где производится поиск и замена
# \1 - первая круглая скобка #### \2 - вторая круглая скобка #### \3 - третья круглая скобка


#################################### Рекурсия
# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove("  Hello\tWorld   "))
#########################################

# Isinstance(объект, класс(выбор)) - Выводит значение булево, является ли объект - строкой, или числовым значением, или чем то другим
#===================================================
# Point - это название класса
# Issublclass(тип класса "Point", object) - возвращает булево значение, является ли данный класс - подклассом
#=====================================================
####################################  Магические методы  ##############################################################
# 1 )  __init__
# __init__  - инициализатор переменных, пример :
# def __init__(self, name, surname):
#     self.name = name
#     self.surname = surname

###################################### Модификаторы доступа : ###################
# public (self.переменная)- публичное свойство
# protected (self._переменная) - используется при наследовании, защищенное за пределами, обращаться только внутри класса
# private (self.__переменная)- закрытые свойства
# x = property(__get_x, __set_x, __del_x)  - сначала get, далее set, и del
####################################################


######################################  Декораторы + Классы #################################################################
# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property      - основной синтаксис property, тот же getter
#     def kg(self):
#         return self.__kg
#
#     @kg.setter     - один из методов - setter, название функции должно быть такое же, как в property
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами')
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pounds(), 'фунтов')
# weight.kg = 41
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pounds(), 'фунтов')

# super() -           вызов метода из родительского класса
# DRY (Dont Repeate Yourself) - не повторяйся, код лучше не дублировать
# класс.mro() - mro - выводит список последовательностей элементов в классе
# print(f'= {elem.convert_to_rub():.2f}') - .2f - это прописывает после точки 2 знака, касательно дробных чисел


######################################### Перегрузка методов ##########################################################
##############################################  Миксин #########################################################
# Миксин - концепция программирования, где класс предоставляет функциональные возможности, но не предназначен для отдельного использования -
# предназначены для убирания дублирования кода


#3#########################################     Pickle and JSON   #####################################################
# #############################################    Кодирование (Сериализация)
# 1) Pickle -
# 2) JSON
# Dump('имя переменной для записи', 'как новая переменная') - сохраняет данные в файл                                        -  Сохранение
# load() - загрузка файла и считывание данных из открытого файла          -  Загрузка

# Dumps(ensure_ascii - меняет кодировку) - сохраняет данные в строку(в памяти)                           -  Сохранение
# loads() - считывание данных из строки (памяти)                          -  Загрузка