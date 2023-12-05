# # import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
#
# todos_by_user = {}
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
#
# def ind(x):
#     return x[1]

#
# top_user = sorted(todos_by_user.items(), key=ind, reverse=True)
# max_complete = top_user[0][1]
#
# users = []
# for user, num_complete in top_user:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# # print(users)
# max_users = ' and '.join(users)
# s = 's' if len(users) > 1 else ""
# print(f"User{s} {max_users} completed {max_complete} TODOS")
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
#
# with open('filtered_data_file.json', 'w') as f:
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, f, indent=2)
#
# with open('filtered_data_file.json', 'r') as f:
#     data = json.load(f)
#     print(data)
# =======================================================================================================================
# import csv

# =======================================================================================================================
####################  CSV(Comma Separated Values) - переменные, разделенные запятыми  ##################################
# import csv
#####################################    list.reader  ###################################
# with open('data.csv', 'r', encoding='UTF-8') as r_file:
#     file_reader = csv.reader(r_file, delimiter=",")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит какие то столбцы: {', '.join(row)}")
#         else:
#             print(f"    {row[0]} - {row[1]}. Родился в {row[2]}")
#         count += 1
#     print(f"Всего строк в файле - {count}")
##########################################################################################

################################    dict.reader          ###############################
# with open('data.csv', 'r', encoding='UTF-8') as r_file:
#     field_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=",", fieldnames=field_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит какие то столбцы: {', '.join(row)}")
#         print(f"    {row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']}")
#         count += 1
#     print(f"Всего строк в файле - {count}")
# =======================================================================================================================

##=======================================================================================================================
# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=',', lineterminator='\r')
#     writer.writerow(['Имя', 'Класс', 'Возраст'])
#     writer.writerow(['Женя', '5', '11'])
#     writer.writerow(['Алекс', '9', '15'])
#     writer.writerow(['Диана', '12', '18'])
# =======================================================================================================================
#    CSV WRITER
# =======================================================================================================================
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
# with open('data_sv.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=',', lineterminator='\r')
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open('data_sv.json', 'r') as f:
#     print(f.read())
# =======================================================================================================================
#    CSV DICTWRITER
# =======================================================================================================================
# with open('stud.csv', 'w') as f:
#     names = ['Имя', "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=',', lineterminator='\r', fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({'Имя': "Саша", "Возраст": "6"})
#     file_writer.writerow({'Имя': "Алекс", "Возраст": "15"})
#     file_writer.writerow({'Имя': "Ион", "Возраст": "10"})
# =======================================================================================================================

# =======================================================================================================================
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
# with open("dict_writer.csv", 'w') as f:
#     dict_writer = csv.DictWriter(f, delimiter=',', lineterminator='\r', fieldnames=data[0].keys())
#     dict_writer.writeheader()
#     for d in data:
#         dict_writer.writerow(d)
# =======================================================================================================================

# =======================================================================================================================
##########################################       Парсинг      ##########################################################
# from bs4 import BeautifulSoup
# import re
# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois').text.strip()
#     if 'Copywriter' in whois:
#         return tag
#     return None


# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# copywriter = []
# row = soup.findAll('div', class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)
# ========================================================================================================================

# ========================================================================================================================
# row = soup.findAll('div', class_='name')
# row = soup.find_all('div', class_='name')
# for r in row:
#     print(r.text)
# print(row)

# row = soup.findAll('div', class_='row')[1].find('div', class_='links')
# print(row)
# row = soup.findAll('div', {'data-set': 'salary'})
# print(row)
# row = soup.find('div', string='Alena').parent.parent
# row = soup.find('div', string='Alena').find_parent(class_='row')
# print(row)
# row = soup.find('div', id='whois3').find_previous_sibling()
# print(row)
# =======================================================================================================================

# =======================================================================================================================
# def get_dig(tag):
#     pattern = r'\d+'
#     res = re.search(pattern, tag).group()
#     print(res)
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# salary = soup.find_all('div', {'data-set': 'salary'})
# for i in salary:
#     get_dig(i.text)
# =======================================================================================================================

# =======================================================================================================================
# import requests


# re = requests.get('https://ru.wordpress.org/')
# print(re.headers)
# print(re.headers['Content-Type'])
# print(re.content)
# print(re.text)

# =======================================================================================================================
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find('header', id='masthead').find('p', class_='site-title').text
#     return p1
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# ======================================================================================================================
# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refind(s):
#     res = re.sub(r'\D+', "", s)
#     return res
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f)
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('section', class_='plugin-section')[3]
#     plugins = p1.find_all('article')
#
#     for plugin in plugins:
#         name = plugin.find('h3').text
#         url = plugin.find('h3').find('a')['href']
#         rating = plugin.find('span', class_='rating-count').find('a').text
#         r = refind(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#     # return len(plugins)
#
#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     # print(get_data(get_html(url)))
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()
# ======================================================================================================================

# ========================================================================================================================
#####import requests
# from bs4 import BeautifulSoup
# import csv
# import re
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def refine_snippet(snippet):
#     return re.sub(r'[❤🐰✅👏🇨🇳🎬🧱]', '', snippet)
#
# ф
# def write_csv(data):
#     with open("plugins(new).csv", 'a') as f:
#         writer = csv.writer(f, lineterminator='\r')
#         writer.writerow((data['name'],
#                          data['url'],
#                          data['snippet'],
#                          data['version']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all('article', class_='plugin-card')
#     for element in elements:
#         try:
#             name = element.find('h3').text
#         except ValueError:
#             name = ""
#         try:
#             url = element.find('a')['href']
#         except ValueError:
#             url = ""
#         try:
#             snippet = element.find('div', class_='entry-excerpt').text.strip()
#             snippet1 = refine_snippet(snippet)
#         except ValueError:
#             snippet1 = ""
#         try:
#             c = element.find('span', class_='tested-with').text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ""
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet1,
#             'version': cy
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(22, 23):
#         url = f'https://ru.wordpress.org/plugins/browse/blocks/page/{i}/'
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()
# from parsers import Parsers
#
#
# def main():
#     pars = Parsers('https://www.ixbt.com/live/index/news/', 'new.txt')
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()
##################################      MVC      #######################################################################
# M - Model(модель)
# V - View(вид или представление)
# C - Controller(контроллер)
# ==========================              SQL             ===============================================================
# Столбы (поля, аттрибуты)
# Строки (записи, кортежи)
# import sqlite3 as sq

# con = sq.connect('profile.db')
# cur = con.cursor()
#
# cur.execute("""
# """)
# con.close()
# =======================================================================================================================
# with sq.connect('profile.db') as con:
#     cur = con.cursor()
#     # cur.execute(""" CREATE TABLE IF NOT EXISTS users (
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # data BLOB
#     # )""")
#     cur.execute("DROP TABLE users")
# with sq.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE my_name(
#     name TEXT
#     )""")
# =======================================================================================================================
# cur.execute("""
# CREATE TABLE IF NOT EXISTS person (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# phone BLOB NOT NULL DEFAULT '+37368000000',
# age INTEGER NOT NULL CHECK(age>15 AND age<70),
# email TEXT UNIQUE
# )""")
# =======================================================================================================================

# with sq.connect('db_3.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM T1
#     ORDER BY FName
#     LIMIT 2, 5
#     """)

# res = cur.fetchone()
# res2 = cur.fetchmany()
# # print(res)
# print(res2)
# res = cur.fetchall()      # 1 Аналог
# print(res)
# for res in cur:           # 2 аналог
#     print(res)
# =======================================================================================================================
# with sq.connect('db_5.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#
#
#     """)
# import sqlite3 as sq
# cars = [
#     ('BMW', 550000),
#     ('Chevrolet', 750000),
#     ('Lamborghini', 900000),
#     ('Daewoo', 450000),
#     ('Honda', 25000)
# ]
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )""")
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)
# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})    # : - показывает имя
# cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

# for car in cars:
#     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)                   #  Аналог

# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 20000)")
# cur.execute("INSERT INTO cars VALUES(2, 'Skoda', 50000)")
# cur.execute("INSERT INTO cars VALUES(3, 'Mitsubishi', 35000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Opel', 95000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Volkswagen', 100000)")

# con.commit()
# con.close()
# =======================================================================================================================

# =======================================================================================================================
# con = None
# try:
#     con = sq.connect('cars.db')
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 20000);
#     UPDATE cars SET price = price + 100
#     """)
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print(f"Ошибка выполнения запроса! {e}")
# finally:
#     if con:
#         con.close()
# =======================================================================================================================

# =======================================================================================================================
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )""")
#
#     cur.execute("SELECT model, price FROM cars")
#     # rows = cur.fetchall()
#     # rows = cur.fetchone()
#     # rows = cur.fetchmany(5)
#     # for row in cur:
#     #     print(row)
#     for res in cur:
#         print(res['model'], res['price'])
# =======================================================================================================================

# =======================================================================================================================
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         ava BLOB
#     );
#     """)
#     img = read_ava(1)
#     if img:
#         binary = sq.Binary(img)
#         cur.execute("INSERT INTO users  VALUES (?, ?)", (1, binary))
# =======================================================================================================================

# =======================================================================================================================
# with sq.connect("cars.db") as con:
#     cur = con.cursor()

# with open('sql_dump.sql', 'w') as f:
#     for sql in con.iterdump():                                    #  Сохранение данных в sql документ
#         f.write(sql)

# with open('sql_dump.sql', 'r') as f:
#     sql = f.read()                                                  #  Восстановление базы данных из sql документа
#     cur.executescript(sql)
# Шаблонизатор (Jinja)
# from jinja2 import Template

# name = "Игорь"
# age = 28
# per = {"name": "Игорь", 'age': 28}
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#
# per = Person("Игорь", 28)
# =================================
# cities = [
#     {'id': 1, 'city': "Moscow"},
#     {'id': 2, 'city': "Chisinau"},
#     {'id': 3, 'city': "Rome"},
#     {'id': 4, 'city': "Ribnita"},
#     {'id': 5, 'city': "Odessa"}
# ]
#
# link = """<select name="cities">
# {% for c in cities -%}
# {% if c.id > 3 -%}
#     <option value='{{ c.id }}'>{{ c['city'] }}</option>
# {% elif c.city == "Moscow" -%}
#     <option>{{ c['city'] }}</option>
# {% else -%}
#     {{ c['city'] }}
# {% endif -%}
# {% endfor -%}
# </select>"""
# info = [
#     {'id': 'index', 'inf': "Главная"},
#     {'id': 'news', 'inf': "Новости"},
#     {'id': 'about', 'inf': "О компании"},
#     {'id': 'shop', 'inf': "Магазин"},
#     {'id': 'contacts', 'inf': "Контакты"}
# ]
# link = """<ul name='info'>
# {% for i in info -%}
# {% if i.inf=="Главная" -%}
#     <li><a href='/{{ i.id }}' class="active">{{ i.inf }}</a></li>
# {% else -%}
#     <li><a href=/{{ i.id }}>{{ i.inf }}</a></li>
# {% endif -%}
# {% endfor -%}
# </ul>"""
# tm = Template(link)
# msg = tm.render(info=info)
#
# print(msg)
# =======================================================================================================================

# =======================================================================================================================
# cars = [
#     {'model': "Audi", 'price': 23000},
#     {'model': "Skoda", 'price': 17300},
#     {'model': "Renault", 'price': 44300},
#     {'model': "Volkswagen", 'price': 21300}
# ]
# sum1 = 0
# for i in cars:
#     sum1 += i['price']
# print(sum1)
# tp1 = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
# tp1 = "{{ cs | random }}"
# tp1 = '{{ cs | replace("Audi", "Bentley") }}'
# tm = Template(tp1)
# msg = tm.render(cs=cars)
# print(msg)
# =======================================================================================================================

# =======================================================================================================================
# html = """
# {% macro input(name, value='', type='text', size=20) -%}
#     <input type='{{ type }}' name='{{ name }}' value='{{ value }}' size='{{ size }}'>
# {% endmacro -%}
# <p>{{ input('username', "Ann") }}</p>
# <p>{{ input('email') }}</p>
# <p>{{ input('password', type='password') }}</p>
# """
# html = """{% macro func(name, placeholder='', type='text') -%}
#     t = type + 1
#     <input type='{{ type }}' name='{{ name }}' placeholder='{{ placeholder }}'>
# {% endmacro %}
#
# <p>{{ func('firstname', 'Имя') }}</p>
# <p>{{ func('lastname', 'Фамилия') }}</p>
# <p>{{ func('address', 'Адрес') }}</p>
# <p>{{ func('phone', type='tel', placeholder='Телефон') }}</p>
# <p>{{ func('email', 'Почта', 'email') }}</p>
# """
# persons = [
#     {'name': "Алексей", "year": 18, 'weight': 78.5},
#     {'name': "Никита", "year": 28, 'weight': 82.3},
#     {'name': "Виталий", "year": 33, 'weight': 94}
# ]
# html = """
# {% macro list_users(list_of_users) -%}
# <ul>
#     {% for u in list_of_users -%}
#         <li>{{ u.name }} {{ caller(u) }}</li>
#     {% endfor %}
# </ul>
# {% endmacro %}
#
# {% call(user) list_users(users) %}
#     <ul>
#         <li>{{ user.year }}</li>
#         <li>{{ user.weight }}</li>
#     </ul>
# {% endcall %}
# """
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)

# =============================================================================================================================

# =============================================================================================================================
# from jinja2 import Environment, FileSystemLoader

# persons = [
#     {'name': "Алексей", "year": 18, 'weight': 78.5},
#     {'name': "Никита", "year": 28, 'weight': 82.3},
#     {'name': "Виталий", "year": 33, 'weight': 94}
# ]
# subs = ['Культура', 'Наука', 'Политика', 'Спорт']
# file_loader = FileSystemLoader("templates")
# env = Environment(loader=file_loader)
#
# tm = env.get_template('about.html')
# msg = tm.render(list_table=subs)
#
# print(msg)
# ===============================================================================================================================
# FLASK
# ===============================================================================================================================

# weight_kg = float(input())
# height_m = float(input())
#
# bmi = weight_kg / (height_m ** 2)
#
# if 18.5 < bmi < 25:
#     print('Оптимальная масса')
# elif bmi < 18.5:
#     print('Недостаточная масса')
# elif 25 < bmi:
#     print('Избыточная масса')
#

#
# num = int(input())
# number_str = str(num)
# reversed_number_str = number_str[::-1]
#
# print(reversed_number_str)


# num = str(int(input()))
# list = []
# while num:
#     list.append(num[-3:])
#     num = num[:-3]
# format = ','.join(reversed(list))
# print(format)


# num = input()
# for idx in range(len(num) - 3, -1, -3):
#     num = num[:idx] + ',' + num[idx:]
# print(num)


# def last_person_standing(n, k):
#     last_person = 0
#     for i in range(2, n + 1):
#         last_person = (last_person + k) % i
#     return last_person + 1
#
#
# n = int(input())
# k = int(input())
#
# # Определение последнего оставшегося человека
# result = last_person_standing(n, k)
# print(result)


# n = int(input("Введите количество точек: "))
#
# # Инициализация счетчиков для каждой четверти
# quadrant1 = quadrant2 = quadrant3 = quadrant4 = 0
#
# # Ввод координат для каждой точки и подсчет четверти
# for i in range(n):
#     x = float(input(f"Введите x-координату для точки {i + 1}: "))
#     y = float(input(f"Введите y-координату для точки {i + 1}: "))
#
#     if x > 0 and y > 0:
#         quadrant1 += 1
#     elif x < 0 < y:
#         quadrant2 += 1
#     elif x < 0 and y < 0:
#         quadrant3 += 1
#     elif y < 0 < x:
#         quadrant4 += 1
#
# # Вывод результата
# print(f"Количество точек в I четверти: {quadrant1}")
# print(f"Количество точек в II четверти: {quadrant2}")
# print(f"Количество точек в III четверти: {quadrant3}")
# print(f"Количество точек в IV четверти: {quadrant4}")
# =======================================================================================================================


# from tkinter import *
# import random
#
# GAME_WIDTH = 700
# GAME_HEIGHT = 700
# SPEED = 150
# BODY_PARTS = 3
# SPACE_SIZE = 50
# SNAKE_COLOR = 'green'
# FOOD_COLOR = 'red'
# BACKGROUND_COLOR = 'black'
#
#
# class Snake:
#     def __init__(self):
#         self.body_size = BODY_PARTS
#         self.coordinates = []
#         self.squares = []
#
#         for i in range(0, BODY_PARTS):
#             self.coordinates.append([0, 0])
#
#         for x, y in self.coordinates:
#             square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag='snake')
#             self.squares.append(square)
#
#
# class Food:
#
#     def __init__(self):
#         x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
#         y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
#
#         self.coordinates = [x, y]
#
#         canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
#
#
# def next_turn(snake, food):
#     x, y = snake.coordinates[0]
#
#     if direction == 'up':
#         y -= SPACE_SIZE
#     elif direction == 'down':
#         y += SPACE_SIZE
#     elif direction == 'left':
#         x -= SPACE_SIZE
#     elif direction == 'right':
#         x += SPACE_SIZE
#
#     snake.coordinates.insert(0, (x, y))
#
#     square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
#
#     snake.squares.insert(0, square)
#
#     if x == food.coordinates[0] and y == food.coordinates[1]:
#         global score
#         score += 1
#
#         label.config(text='Score:{}'.format(score))
#
#         canvas.delete('food')
#
#         food = Food()
#
#     else:
#         del snake.coordinates[-1]
#
#         canvas.delete(snake.squares[-1])
#
#         del snake.squares[-1]
#     if check_collisions():
#         game_over()
#     else:
#         window.after(SPEED, next_turn, snake, food)
#
#
# def change_direction(new_direction):
#     global direction
#
#     if new_direction == 'left':
#         if direction != 'right':
#             direction = new_direction
#     elif new_direction == 'right':
#         if direction != 'left':
#             direction = new_direction
#     elif new_direction == 'up':
#         if direction != 'down':
#             direction = new_direction
#     elif new_direction == 'down':
#         if direction != 'up':
#             direction = new_direction
#
#
# def check_collisions():
#     x, y = snake.coordinates[0]
#
#     if x < 0 or x >= GAME_WIDTH:
#         return True
#     elif y < 0 or y >= GAME_HEIGHT:
#         return True
#
#     for body_part in snake.coordinates[1:]:
#         if x == body_part[0] and y == body_part[1]:
#             print('Game over')
#             return True
#
#     return False
#
#
# def game_over():
#     canvas.delete(ALL)
#     canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text='GAME OVER',
#                        fill='red', tag='gameover')
#
#
# window = Tk()
# window.title('Snake Game')
# window.resizable(False, False)
#
# score = 0
# direction = 'down'
#
# label = Label(window, text='Score:{}'.format(score), font=('consolas', 40))
# label.pack()
#
# canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
# canvas.pack()
#
# window.update()
#
# window_width = window.winfo_width()
# window_height = window.winfo_height()
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()
#
# x = int((screen_width / 2) - (window_width / 2))
# y = int((screen_height / 2) - (window_height / 2))
#
# window.geometry(f'{window_width}x{window_height}+{x}+{y}')
#
# window.bind('<Left>', lambda event: change_direction('left'))
# window.bind('<Right>', lambda event: change_direction('right'))
# window.bind('<Up>', lambda event: change_direction('up'))
# window.bind('<Down>', lambda event: change_direction('down'))
#
# snake = Snake()
# food = Food()
#
# next_turn(snake, food)
#
# window.mainloop()
# ========================================================================================================================

# SEND EMAIL
# import smtplib
#
# # header
# sender = 'sender@gmail.com'
# receiver = 'receiver@gmail.com'
# password = 'password123'
# subject = 'Python email test'
# body = 'I Wrote an email'
#
# message = f'''From: Alexandru Spr{sender}
# To:Nicolas Cage{receiver}
# subject: {subject}\n
# {body}
# '''
#
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# try:
#     server.login(sender, password)
#     print('Logged in')
#     server.sendmail(sender, receiver, message)
#     print('Email has been sent')
# except smtplib.SMTPAuthenticationError:
#     print('unable to sign in')

#=======================================================================================================================


