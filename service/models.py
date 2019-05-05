from django.db import models
from django.conf import settings
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse

# Create your models here.
class services (models.Model):

    type=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=300)
    price=models.PositiveIntegerField()
    phone=models.CharField(max_length=11)
    address=models.CharField(max_length=30)

    def _str_(self):
        return self.name


    def get_api_url(self, request=None):
        return api_reverse('getservice',kwargs={'id':self.id}, request=request)
