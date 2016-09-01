from rest_framework import serializers
from core.models import Item, ItemList



class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'title', 'list', 'created_date', 'due_date', 'completed', 'completed_date', 'note', 'priority')
