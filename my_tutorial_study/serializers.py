from rest_framework import serializers
from my_tutorial_study.models import Book
from django.contrib.auth.models import User


class BookModelSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.name")
    class Meta:
        model = Book
        fields = "title", "author","price","user"


class BookSchema(serializers.Serializer):
    title = serializers.CharField(max_length=10)
    author = serializers.CharField(max_length=10)
    price = serializers.IntegerField()
    user = serializers.ReadOnlyField(source="user.name")

    """ create 재정의 """
    def create_a(self, **validated_data):
        return Book.objects.create(**validated_data)
    
    """ update 재정의 """
    def update(self, instance, **validated_data):
        title = instance.title = validated_data.get("title", instance.title)
        author = instance.author = validated_data.get("author", instance.author)
        price = instance.price = validated_data.get("price", instance.price)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'books']