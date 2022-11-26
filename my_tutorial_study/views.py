from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from my_tutorial_study.models import Book
from my_tutorial_study.serializers import BookModelSerializer, BookSchema

@api_view(["GET", "POST"])
def book_get_post(request):
    """
    모든 book_list를 출력한다.
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookModelSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = BookModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    """
    특정 객체에 대한 조회, 업데이트, 삭제
    """
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookModelSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = request.data
        serializer = BookModelSerializer(book, data=data, partial=True) # serializer에 객체와 데이터를 모두 넘겨준다.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(["GET", "POST"])
def book_get_post(request):
    """
    모든 book_list를 출력한다.
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSchema(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = BookSchema(data=data)
        if serializer.is_valid():
            serializer.create(**serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def book_detail(request, pk):
    """
    특정 객체에 대한 조회, 업데이트, 삭제
    """
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = BookSchema(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = request.data
        serializer = BookSchema(book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.update(book, **data) # 시리얼라이저는 단순히 확인용이고 들어오는 데이터를 넣어준다.
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)