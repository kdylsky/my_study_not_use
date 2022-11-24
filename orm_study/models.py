from django.db import models

class User(models.Model):
    name = models.CharField(max_length=10)
    class Meta:
        db_table = "users"


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age  = models.IntegerField()
    class Meta:
        db_table = "userinfo"


class Category(models.Model):
    name = models.CharField(max_length=10)
    class Meta:
        db_table = "categorys"


class SubCategory(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    class Meta:
        db_table = "subcategory"


class Product(models.Model):
    name = models.CharField(max_length=10)
    class Meta:
        db_table = "products"


class Order(models.Model):
    products = models.ManyToManyField(Product)
    number = models.IntegerField()
    class Meta:
        db_table = "orders"