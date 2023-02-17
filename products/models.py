from email.policy import default
from random import choices
from ssl import Options
from django.db import models

# Create your models here.

class Mobiles(models.Model):
    name=models.CharField(max_length=200)
    brand=models.CharField(max_length=100,null=True)
    price=models.PositiveIntegerField(default=1000)
    options=(
        ("5g","5g"),
        ("4g","4g"),
        ("3g","3g")
    )
    band=models.CharField(max_length=200,choices=options,default="4g")
    doptions=(
        ("led","led"),
        ("amoled","amoled"),
    )
    display=models.CharField(max_length=200,choices=doptions,default="led")

    def __str__(self):
        return self.name