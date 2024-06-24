from rest_framework import serializers
from .models import Talaba,Guruh


class TalabaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talaba
        fields = '__all__'
        
        
class GuruhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guruh
        fields = '__all__'