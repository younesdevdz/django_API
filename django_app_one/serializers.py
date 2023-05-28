
from rest_framework import serializers

from django_app_one.models import Breakdown , Reporting 


class BreakdownSerializer (serializers.ModelSerializer):
    class Meta :
        model = Breakdown
        fields =('__all__')
class ReportingSerilalizer (serializers.ModelSerializer):
    class Meta :
        model = Reporting
        fields= ('__all__')


