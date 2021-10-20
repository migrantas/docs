from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

class Grajdanstvo(models.Model):
    mvd = models.CharField(max_length=53,default="ГУ МВД России по г. Москве")



