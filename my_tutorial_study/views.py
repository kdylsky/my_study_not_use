from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from my_tutorial_study.models import Book
from my_tutorial_study.serializers import BookModelSerializer, BookSchema


@csrf_exempt
def book_get_post(request):
    """
    모든 book_list를 출력한다.
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookModelSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def book_detail(request, pk):
    """
    특정 객체에 대한 조회, 업데이트, 삭제
    """
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BookModelSerializer(book)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BookModelSerializer(book, data=data, partial=True) # serializer에 객체와 데이터를 모두 넘겨준다.
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)



@csrf_exempt
def book_get_post(request):
    """
    모든 book_list를 출력한다.
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSchema(books, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSchema(data=data)
        if serializer.is_valid():
            serializer.create(**serializer.data)
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def book_detail(request, pk):
    """
    특정 객체에 대한 조회, 업데이트, 삭제
    """
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BookSchema(book)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BookSchema(book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.update(book, **data) # 시리얼라이저는 단순히 확인용이고 들어오는 데이터를 넣어준다.
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)