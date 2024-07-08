from django.db import models

# Create your models here.

class Setka(models.Model):
    ves = models.FloatField(default=3.8)
    dlina_setki = models.FloatField(default=1500)
    untill = models.CharField(max_length=10,default="cm")
    razmer_sechenya = models.FloatField(default=3.6)
    unitrs = models.CharField(max_length=10,default="mm")
    price = models.DecimalField(max_digits=10,decimal_places = 2 )
