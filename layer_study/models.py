from django.db import models




# class Number(models.Model):
#     CHOICE_NUMBER =(
#         ("P", "Positive Number"),
#         ("N", "Negative Numer"),
#         ("Z", "Zero")
#     )
#     number = models.IntegerField()
#     text   = models.CharField(max_length=1, choices=CHOICE_NUMBER, blank=True, default=" ")

#     class Meta:
#         db_table="numbers"
    
#     def set_text(self, number):
#         if number < 0:
#             self.text = "N"
#         elif number == 0:
#             self.text = "Z"
#         else:
#             self.text = "P"
#         self.save()





class NumberQuerySet(models.QuerySet):
    def set_text(self):
        if self[0].number < 0:
            msg = "N"
        elif self[0].number == 0:
            msg = "Z"
        else:
            msg = "P"
        return msg 


class Number(models.Model):
    CHOICE_NUMBER =(
        ("P", "Positive Number"),
        ("N", "Negative Numer"),
        ("Z", "Zero")
    )
    number = models.IntegerField()
    text   = models.CharField(max_length=1, choices=CHOICE_NUMBER, blank=True, default=" ")

    class Meta:
        db_table="numbers"
    
    objects = NumberQuerySet.as_manager()
   



