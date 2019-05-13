from django.test import TestCase
from .models import services
from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework.reverse import reverse as api_reverse
# Create your tests here.
class ServicesAPITestCase(APITestCase):

     def test_get_services(self):
         data={}
         url= api_reverse("postservice")
         response=self.client.get(url,data,format='json')
         self.assertEqual(response.status_code,status.HTTP_200_OK)
         print(response.data)

     def test_post_service(self):
         data={"type":"serv","name":"hola","description":"esto es","price":"35", "phone":"una", "address":"prueba"}
         url= api_reverse("postservice")
         response=self.client.post(url,data,format='json')
         self.assertEqual(response.status_code,status.HTTP_200_OK)
         print(response.data)

     def test_get_service(self):
         data={}
         url= api_reverse("getservice", args=['2da76876-420e-4497-bdfe-528f8e10714e'])
         response=self.client.get(url,data,format='json')
         self.assertEqual(response.status_code,status.HTTP_200_OK)
         print(response.data)

     def test_put_service(self):
         data = {"id":"1d04996d-1d61-40f5-8738-13cd37b4f230","Type":"servicio","Name":"parkibike","Description":"tarifa por minuto","Price":"60", "Phone":"+54 3785643", "Address":"calle 23#56-34"}
         url= api_reverse("getservice", args=['2da76876-420e-4497-bdfe-528f8e10714e'])
         response=self.client.put(url,data,format='json')
         self.assertEqual(response.status_code,status.HTTP_200_OK)
         print(response.data)

     def test_delete_service(self):
         data={}
         url = api_reverse("getservice", args=['a1631e8e-f202-4e3d-99b8-0ce5ce696a24'])
         response = self.client.delete(url, data, format='json')
         self.assertEqual(response.status_code, status.HTTP_200_OK)
         print(response.data)