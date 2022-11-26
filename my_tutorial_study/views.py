from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from my_tutorial_study.models import Book
from my_tutorial_study.serializers import BookModelSerializer, BookSchema
from django.http import Http404


class BookAPI(APIView):
    def get(self, requets):
        books = Book.objects.all()        
        serializer = BookModelSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = BookModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailBookAPI(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookModelSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        data = request.data
        serializer = BookModelSerializer(book, data=data, partial=True) # serializer에 객체와 데이터를 모두 넘겨준다.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSchema(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = BookSchema(data=data)
        if serializer.is_valid():
            serializer.create(**serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailBookAPI(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSchema(book) 
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        data = request.data
        serializer = BookSchema(book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.update(book, **data) # 시리얼라이저는 단순히 확인용이고 들어오는 데이터를 넣어준다.
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

