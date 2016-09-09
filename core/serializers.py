from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from core.models import Item, ItemList
import datetime


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    permissions = serializers.SlugRelatedField(
        many=True,
        slug_field='codename',
        queryset=Permission.objects.all()
    )

    class Meta:
        model = Group
        fields = ('url', 'name', 'permissions')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    def post_save(self, obj, created=False):
        """
        On creation, replace the raw password with a hashed version.
        """
        if created:
            obj.set_password(obj.password)
            obj.save()

    class Meta:
            model = User
            view_name = 'users:user-detail'
            fields = ('url', 'username', 'password', 'groups', 'email', 'first_name', 'last_name', 'is_superuser')


class ItemSerializer(serializers.ModelSerializer):

    list = serializers.SlugRelatedField(queryset=ItemList.objects.all(), slug_field="slug")

    def create(self, validated_data):
        validated_data['created_date'] = datetime.datetime.now()
        print(validated_data)
        item = Item.objects.create(**validated_data)
        item.save()
        return item

    class Meta:
        model = Item
        fields = ('id', 'title', 'list', 'created_date', 'due_date', 'completed', 'completed_date', 'note', 'priority')


class ItemListSerializer(serializers.HyperlinkedModelSerializer):
    owner = UserSerializer()
    item = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='item-detail')


    class Meta:
        model = ItemList
        fields = ('id', 'title', 'slug', 'created_date', 'due_date', 'completed', 'completed_date', 'owner', 'item')



