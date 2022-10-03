from django.db import models

class Artiles(models.Model):
    title= models.CharField('Название',max_length=50,default='')
    anons = models.CharField('Анонс', max_length=250, default='')
    full_text= models.TextField('Полный текст')
    date= models.DateTimeField('Дата публикации')

    def __str__(self):
        return  f'Новость:{self.title}'

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'