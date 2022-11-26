from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=10)
    author = models.CharField(max_length=10)
    price = models.IntegerField()

    class Meta:
        db_table = "books"