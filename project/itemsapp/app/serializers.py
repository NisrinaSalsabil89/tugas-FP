from rest_framework import serializers
from app.models import ItemsModel
 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsModel
        fields = ['name','price']