from __future__ import print_function
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from service.models import services
from .serializers import servicesSerializer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
import uuid, os, base64
import boto3, datetime
from boto3.dynamodb.conditions import Key
import json
from botocore.exceptions import ClientError

region = os.environ.get( 'AWS_DEFAULT_REGION' )
dynamodb = boto3.resource( 'dynamodb', region_name='us-west-2')
tabla_Services = dynamodb.Table('Services' )

class servicesCreateListView(APIView):
    lookup_field = 'pk'
    serializer_class = servicesSerializer
    #queryset = services.object.all()

    def get(self,request):
        respuesta = tabla_Services.scan()
        return Response(respuesta['Items'])

    def post(self,request):

        UUID=uuid.uuid4()
        number=str(UUID)
        #dat=json.loads(request.data)
        #dit=json.dumps(request.data)
        #print (json.loads(request.data))
        #print (json.loads(request.data)['type'])
        #print(json.dumps(request.data)[1])
        #number=5
        datos_servicio = {
                'id':number,
                'Type': request.data['type'],
                'Name': request.data['name'],
                'Description': request.data['description'],
                'Price': request.data['price'],
                'Phone': request.data['phone'],
                'Address': request.data['address']
            }
        respuesta = tabla_Services.put_item(Item=datos_servicio)
        if (respuesta['ResponseMetadata']['HTTPStatusCode'] == 200):
             respuesta = tabla_Services.scan()
        return Response('Servicio creado correctamente')
        #return Response(respuesta['Items'])

    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}


class servicesRetrieveUpdateDestroyView(APIView):
    lookup_field = 'id'
    #serializer_class = servicesSerializer
    #queryset = services.objects.all()

    def get(self,request,id):
        try:
            respuesta = tabla_Services.get_item(
                Key={
                    'id': id
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            response=respuesta['Item']
            return Response(response, status=status.HTTP_200_OK)
            #return Response (json.dumps(response,indent=4, default=json_util.default))

    def delete(self,request,id):
        try:
            response = tabla_Services.delete_item(
                Key={
                    'id': id
                }
            )

        except ClientError as e:
            if e.response['Error']['Code'] == "ConditionalCheckFailedException":
                print(e.response['Error']['Message'])
            else:
                raise
        else:
            return Response ('El servicio ha sido eliminado')

    def put(self,request,id=None):
        try:
            response = tabla_Services.update_item(
                Key={
                    'id': id
                },
                UpdateExpression="set #ty = :t, #na = :n, #des = :d, #pr = :pr, #ph =:ph, #ad = :a",
                ExpressionAttributeValues={
                    ":t": request.data['Type'],
                    ":n": request.data['Name'],
                    ":d": request.data['Description'],
                    ":pr": request.data['Price'],
                    ":ph": request.data['Phone'],
                    ":a": request.data['Address'],
                },
                ExpressionAttributeNames={
                    "#ty": "Type",
                    "#na": "Name",
                    "#des": "Description",
                    "#pr": "Price",
                    "#ph": "Phone",
                    "#ad": "Address"
                },
                ReturnValues="UPDATED_NEW"
            )

        except ClientError as e:
            if e.response['Error']['Code'] == "ConditionalCheckFailedException":
                print(e.response['Error']['Message'])
            else:
                raise
        else:
            if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
                response = tabla_Services.get_item(
                    Key={
                     'id': id
                    }
                )
            return Response(response['Item'])

    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}


