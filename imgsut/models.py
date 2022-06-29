from django.db import models


class imgs(models.Model):
    title = models.CharField(max_length=50)
    imges = models.ImageField('img/')
