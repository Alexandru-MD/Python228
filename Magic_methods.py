
# __init__  - инициализатор переменных
# __str__ -           магический метод, когда мы обращаемся к экземпляру класса, возвращает данные из него (строковое значение)
#__repr__ -           магический метод вывода строк(как и str), даёт более подробную информацию, чем str
        # return f"{self.__class__}:{self.name}" - пример работы repr
# __mro__ -           магическая переменная, выводит кортеж последовательностей элементов в классе!
# __doc__  - документация любой функции(принцип работы). Синтаксис - """ Любой текст """
# __slots__ - резервирует конкретные переменные, и не позволяет более добавлять переменные в класс где то за пределами(также не даёт наследовать другим классам)
# __len__  - позволяет считать длину символов или параметров
#__sizeof__ - показывает размеры(в байтах)

############################### Удаление, изменение элементов и индексов ###############################################
# __getitem__(self, item) – получение значения по ключу item;
# __setitem__(self, key, value) – запись значения value по ключу key;
# __delitem__(self, key) – удаление элемента по ключу key.

######################################################  Магические методы #########################################################
# __add__ - это метод сложения в классах(x + y).. Используется как замена "+", может складывать классы.. Также есть метод __iadd__(старый метод),
# он позволяет складывать "x+=y", вместо обычному x + y. Есть еще __radd__, тот же принцип сложения
# __sub__  - метод вычитания (x - y)
# __mul__ -  метод умножения (x * y)
# __truediv__  - метод деления с остатком (x / y)
# __floordiv__ - деление без остатка (x // y)
# __mod__ -  остаток от деления (x % y)
#####################
# __eq__ - Оператор равенства  x == y
# __ne__ - оператор неравенства x != y
# ___lt__ - оператор знака меньше
# ___le__ - оператор знака меньше либо равно
# ___gt__ - оператор знака больше
# ___ge__ - оператор знака больше либо равно
##############################

#__call__ - позволяет вызывать экземпляр класса

####  Синтаксис метода get ######
# def __get__(self, instance, owner):
#     return instance.__dict__[self.__name]


# __all__ = [названия переменных для импорта] - магическая переменная, которая прописывается в init( при создании пакета), что б
# выделить все переменные, которые импортируются
# __getstate__ - используется для возвращение ключей сериализации(для метода dumps())
# __setstate__ - используется для метода loads()