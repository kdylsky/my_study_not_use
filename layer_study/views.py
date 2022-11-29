from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from django.http import JsonResponse

from layer_study.serializers import NumberSerializer
from layer_study.service import NumberService

# 모델 비즈니스 로직
# @api_view(["POST"])
# @parser_classes([JSONParser])
# def create_number(request, *args, **kwargs):
#     data = request.data
#     serializer = NumberSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     number = serializer.save()
#     number.set_text(data.get("number"))
#     return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


# 뷰 비즈니스 로직
# @api_view(["POST"])
# @parser_classes([JSONParser])
# def create_number(request, *args, **kwargs):
#     data = request.data
#     serializer = NumberSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     number = serializer.save()

#     if data.get("number") < 0:
#         number.text = "N"
#     elif data.get("number") == 0:
#         number.text = "Z"
#     else:
#         number.text = "P"
#     number.save()

#     return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


# 시리얼라이저 비즈니스 로직
# @api_view(["POST"])
# @parser_classes([JSONParser])
# def create_number(request, *args, **kwargs):
#     data = request.data
#     serializer = NumberSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)



# 서비스 비즈니스 로직
# @api_view(["POST"])
# @parser_classes([JSONParser])
# def create_number(request, *args, **kwargs):
#     data = request.data
#     serializer = NumberSerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     number_obj = serializer.save()
#     number_service = NumberService()
#     number_service.set_text(number_obj)
#     return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


# 쿼리셋정의 비즈니스 로직
from layer_study.models import Number
@api_view(["POST"])
@parser_classes([JSONParser])
def create_number(request, *args, **kwargs):
    data = request.data
    serializer = NumberSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    number_obj = serializer.save()
    text = Number.objects.filter(id = number_obj.id).set_text()
    number_obj.text = text
    number_obj.save()
    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
