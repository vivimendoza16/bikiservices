from rest_framework import serializers
from .models import services

class servicesSerializer (serializers.ModelSerializer):
    class Meta:
        model=services
        fields= '__all__'
        read_only_fields=['pk']

        def validate_name(self,value):
            qs=services.objects.filter(name_iexact=value)
            if self.instance:
               qs= qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError(" Este servicio ya existe")
            return value

        def get_url(self,obj):
            request=self.context.get("request")
            return obj.get_api_url(request=request)
