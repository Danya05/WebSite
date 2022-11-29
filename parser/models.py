from django.db import models


class Coins(models.Model):
    title = models.CharField('Название монеты', max_length=50)
    desription = models.CharField('Описание монеты', max_length=250)
    capitalization = models.IntegerField('Капитализация монеты')
    cost = models.IntegerField('Стоимость 1 монеты')
    date = models.DateTimeField('Время последнего лобновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Монета'
        verbose_name_plural = 'Монеты'
