from django.db import models

# Create your models here.
class News_table(models.Model):
    title = models.CharField('Название', max_length=50, default='Название по умолчанию')
    anons = models.CharField('Анонс', max_length=250, default='Анонс по умолчанию')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'Новость: {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'