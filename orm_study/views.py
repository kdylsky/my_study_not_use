from django.http      import JsonResponse
from django.views     import View
from orm_study.models import (
    User, 
    UserInfo,
    Category,
    SubCategory,
    Product,
    Order
)
from decorators import query_debugger

class UserOrmView(View):
    @query_debugger
    def get(self, request):
        """
        1대1 필드의 경우 외래키가 없는 곳에서도 _set 없이 연결만 되있다면 바로 참조하러 갈수 있다.
        """
        # User기준(역참조)
        # 11번 
        # OneToOne관계에 외래키를 가지고 있지 않은 경우, 일대일 관계이기 때문에 _set없이 바로 참조 가능하다.
        users = User.objects.all()
        users = list(users)
        user  = users[0]
        for user in users:
            user.userinfo.age

        # 1번 
        # OneToOne관계에서 외래키를 가지고 있지 않은 경우에 select_related를 사용해서 최적화
        users = User.objects.select_related("userinfo").all()
        users = list(users)
        user  = users[0]
        for user in users:
            user.userinfo.age



        # UserInfo기준(정참조)
        # 111번
        user_info_list = UserInfo.objects.all()
        for user_info in user_info_list:
            print(user_info.user.name)

        # 1번
        user_info_list = UserInfo.objects.select_related("user").all()
        for user_info in user_info_list:
            print(user_info.user.name)

        # 2번
        user_info_list = UserInfo.objects.all().prefetch_related("user")
        for user_info in user_info_list:
            print(user_info.user.name)

        

        return JsonResponse({"result": "success"}, status=200)   


class CategoryOrmView(View):
    @query_debugger
    def get(self, request):
        # Category기준(역참조)
        # 11번
        # 외래키를 가지고 있지 않은 경우
        categorys = Category.objects.all()
        for category in categorys:
            print(category.subcategory_set.all())
        
        # 2번
        # 외래키를 가지고 있지 않은 경우
        categorys = Category.objects.all().prefetch_related("subcategory_set")
        for category in categorys:
            print(category.subcategory_set.all())
        

        

        # SubCategory기준(정참조)
        # 111번
        subcategorys = SubCategory.objects.all()
        for subcategory in subcategorys:
            print(subcategory.Category.name)

        # 1번
        # 정참조이기 때문에 select_related() 가지고 오는 것이 좋다.
        subcategorys = SubCategory.objects.select_related("Category").all()
        for subcategory in subcategorys:
            print(subcategory.Category.name)
        
        # 2번
        # prefetch_related 가지고 올수는 있지만, 추가 쿼리를 한번 더 날리게 된다.
        subcategorys = SubCategory.objects.all().prefetch_related("Category")
        for subcategory in subcategorys:
            print(subcategory.Category.name)
        

        return JsonResponse({"result": "success"}, status=200)   


class ProductOrmView(View):
    @query_debugger
    def get(self, request):
        """
        ManyToMany관계에서는 prefetch_related만 사용할 수 있다.
        
        M:N 관계에서는 
          - order.products.all()
          - product.order_set.all()
          - 바로 속성으로 참조하지 못한다. 다 가지고와서 해야한다.
        """

        # Product기준(역참조)
        # 101번
        # ManyToMany관계에서 외래키를 가지고 있지 않는 객체를 기준으로
        products = Product.objects.all()
        for product in products:
            print(product.order_set.all())
        
        # 2번
        # ManyToMany관계에서 외래키를 가지고 있지 않는 객체를 기준으로
        products = Product.objects.all().prefetch_related("order_set")
        for product in products:
            print(product.order_set.all())

        


        # Order기준(정참조)
        # 101번
        # ManyToMany관계에서 외래키를 가지고 있는 객체를 기준으로
        orders  = Order.objects.all()
        for order in orders:
            print(order.products.all())

        # 2번
        # ManyToMany관계에서 외래키를 가지고 있는 객체를 기준으로
        orders  = Order.objects.all().prefetch_related("products")
        for order in orders:
            print(order.products.all())

        return JsonResponse({"result": "success"}, status=200)   

