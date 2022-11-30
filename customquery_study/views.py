from django.http import JsonResponse

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes

from customquery_study.serializers import AccountSerializer

from customquery_study.models import Account

@api_view(["POST"])
@parser_classes([JSONParser])
def account_create(request, *args, **kwargs):
    data = request.data
    serializer = AccountSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    obj = serializer.save()
    men = Account.objects.get_men_gender()
    women = Account.objects.get_women_gender()
    Account.objects.filter(id=obj.id).set_generation(data.get("generation"))
    c = Account.objects.get(id=60)
    print(c)
    b = Account.age_objects.all()
    print(b)
    return JsonResponse(True, status=status.HTTP_201_CREATED, safe=False)

    

