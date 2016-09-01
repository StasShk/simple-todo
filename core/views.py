from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework import status, generics
from core.models import ItemList, Item
from core.serializers import ItemSerializer


class ItemsAll(APIView):
    def get(self, request, format=None):
        item = Item.objects.all().order_by('-created_date')
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
