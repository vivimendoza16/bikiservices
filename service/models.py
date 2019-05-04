from django.db import models
from django.conf import settings

# Create your models here.
class services (models.Model):

    type=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=300)
    price=models.PositiveIntegerField()
    phone=models.CharField(max_length=11)
    adress=models.CharField(max_length=30)

    def _str_(self):
        return self.name
