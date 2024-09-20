from rest_framework import serializers
from .models import *

class mymodelserializer(serializers.ModelSerializer):
  class Meta:
    model=mymodel
    fields=['name','age','email','contact']

    def validate_contact(self,value):
      if len(value) != 10:
        raise serializers.ValidationError("contact number be 10 digits")
      return value
    
    def validate_age(self,value):
      if not value > 18:
        raise serializers.ValidationError("age must be 18 or above 18")
      return value

   
        