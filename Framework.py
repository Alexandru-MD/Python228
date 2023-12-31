# from jinja2 import Template
#   Template({{переменная из рендера}}) - конструкция от jinja2
#       {{}} - выражение для вставки конструкций Python в шаблон
#       {% For, if, while %} - спецификатора шаблона
#=======================================================================================================================

#=======================================================================================================================
#       {% for <выражение> %} - спецификатора шаблона
#           <тело цикла>
#               {% endfor %} - обязательно
                        # link = """<select name="cities">
                        # {% for c in cities -%}
                        #     <option value='{{ c.id }}'>{{ c['city'] }}</option>
                        # {% endfor -%}
                        # </select>"""
#=======================================================================================================================

#=======================================================================================================================
                        # {% if <условие> %}
                        # {% else  %}
                        # {% endif  %}
#       {# #} - блок комментариев
#       # ## - строковый комментарий
#   render(Переменная, которая попадает в шаблон Template)  - метод, который указывает что переменная используется в Template
#=======================================================================================================================
                                            #  Call - используется для добавления вложенных элементов
#=======================================================================================================================
# {% call(параметры) <вызов макроса> %}
# <вложенный шаблон>
# {% endcall %}
#=======================================================================================================================
                                    # Подключение html документа
#=======================================================================================================================
# persons = [
#     {'name': "Алексей", "year": 18, 'weight': 78.5},
#     {'name': "Никита", "year": 28, 'weight': 82.3},
#     {'name': "Виталий", "year": 33, 'weight': 94}
# ]
# file_loader = FileSystemLoader("templates")
# env = Environment(loader=file_loader)
#
# tm = env.get_template('main.html')
# msg = tm.render(users=persons)
# print(msg)

# {% include <путь к файлу шаблона> %}

##======================================================================================================================
##======================================================================================================================
##======================================================================================================================
#######################################3              FLASK  ############################################################
# from flask import Flask, render_template, url_for
#
# app = Flask(__name__)
#
# menu = ['Главная страница', 'О нас', 'Обратная связь']
#
#
# @app.route("/")
# @app.route("/index")
# def index():
#     print(url_for("index"))
#     return render_template('index.html', title="Главная", menu=menu)
#
#
# @app.route("/about")
# def about():
#     print(url_for("about"))
#     return render_template('about.html', title="О нас", menu=menu)
#
#
# @app.route("/profile/<int:username>")  --- int, float, string, path
# def profile(username):
#     return f"Пользователь: {username}"
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


# int- целые числа
# float - числа с плавающей точкой
# string - строка
# path - можно использовать любые допустимые символы:
    # URL плюс символ слеша и далее другой путь
# required - поле должно быть обязательно заполнено

# flash - метод для вывода сообщения, что сообщение было отправлено.
    #get_flashed_messages() - функция для получения