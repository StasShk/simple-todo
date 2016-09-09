from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework import status, generics, viewsets
from core.models import ItemList, Item

from django.contrib.auth.models import User, Group

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


from core.serializers import UserSerializer, GroupSerializer, ItemSerializer, ItemListSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ItemList.objects.all()
    serializer_class = ItemListSerializer





