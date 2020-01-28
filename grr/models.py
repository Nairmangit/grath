from django.db import models

# Create your models here.
class test(models.Model):
    tem = models.DecimalField(max_digits=11, decimal_places=4)
    dat = models.DateTimeField()
