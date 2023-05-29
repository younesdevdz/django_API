
from rest_framework import serializers

from django_app_one.models import ProductModel  


class ProductSerialzer (serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields =('__all__')




