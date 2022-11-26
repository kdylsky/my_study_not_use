from rest_framework import serializers
from my_tutorial_study.models import Book
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings



class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookSchema(serializers.Serializer):
    title = serializers.CharField(max_length=10)
    author = serializers.CharField(max_length=10)
    price = serializers.IntegerField()

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