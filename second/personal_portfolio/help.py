# models.CharField(max_length=количество символов) - Поле символов(максимальная длина)

#  Данные для страницы админа
# class Skills(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=250)
#     image = models.ImageField(upload_to='skills/images/')
#     url = models.URLField(blank=True)


# blogs = Blog.objects.order_by('-date')
#     -date - обратное по дате(сверху новое,внизу старое)
#     order_by - сортирует по конкретному параметру

##########################   ФИЛЬТРЫ DJANGO   ####################
# |truncatechars: фильтр для ограничение символов на вывод странички
# |striptags - убирает тэги html на страничках
# |date:'d.m.Y' - настройка даты, в 'пишется свой формат'
# |safe - обрабатывает все тэги, которые в тексте