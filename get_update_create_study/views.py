import json
from django.http import JsonResponse
from django.views import View
from get_update_create_study.models import Student


class StudentView(View):
    def post(self, request, *args, **kwargs):
        """
        get_or_create에서는 
        먼저 default 밖에 있는 값으로 데이터베이스에 객체가 있는지 판단한다.
        만약 있다면 False를 반환하고, 없다면 True를 반환한다.
    
        False이면 default은 아무런 작업을 하지 않는다. 
        True이면 default에 있는 값으로 생성한다.

        default는 객체를 생성할때만 사용된다.
        """
        
        data = json.loads(request.body)
        obj, created = Student.objects.get_or_create(
            name = data["name"],
            email = data["email"],
            age = data["age"],
            defaults={
                "local":data["local"],
                "gender": data["gender"]
            }
        )
        # if not created:
        #     obj.local = data["local"]            
        #     obj.save()
        print(obj)
        print(created)
        return JsonResponse({"result":"success"}, status=200)


class StudentTwoView(View):
    """
    update_or_create에서는 
    먼저 default 밖에 있는 값으로 데이터베이스에 객체가 있는지 판단한다.
    만약 있다면 False를 반환하고, 없다면 True를 반환한다.
    
    False이면 default에 있는 값으로 업데이트 한다.
    True이면 default에 있는 값으로 생성한다.
    """
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        obj, created = Student.objects.update_or_create(
            name = data["name"],
            email = data["email"],
            age = data["age"],
            defaults={
                "local":data["local"],
                "gender": data["gender"]
            }
        )
        return JsonResponse({"result":"success"}, status=200)
