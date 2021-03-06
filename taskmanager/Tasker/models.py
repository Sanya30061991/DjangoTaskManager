from django.db import models

# Create your models here.
class Tasks(models.Model):
    user_id = models.CharField('Айди юзера', max_length=100)
    title = models.CharField('Название', max_length=50)
    desc = models.CharField('Описание', max_length=100)
    fin = models.CharField('Закончено ли', max_length=1)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"