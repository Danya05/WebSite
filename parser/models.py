from django.db import models


class Coins(models.Model):
    title = models.CharField('Название монеты', max_length=50)
    description = models.TextField('Описание монеты')
    capitalization = models.IntegerField('Капитализация монеты')
    cost = models.FloatField('Стоимость 1 монеты')
    date = models.DateTimeField('Время последнего обновления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/parser/{self.id}'

    class Meta:
        verbose_name = 'Монета'
        verbose_name_plural = 'Монеты'


class CoinsParsingResult(models.Model):
    task_id = models.ForeignKey(
        Coins,
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    cost = models.FloatField()
