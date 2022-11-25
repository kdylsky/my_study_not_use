from django.db import models

class Student(models.Model):
    GENDER = (
        ('M', 'Man'),
        ('W', 'Women'),
    )
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    local = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER)
    age  = models.IntegerField()
    
    class Meta:
        db_table = "students"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            if self.gender not in ["M","W"]:
                self.gender="M"
        else:
			# on Update
            pass
        return super(Student, self).save(*args, **kwargs)