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
