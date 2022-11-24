from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    birth_date = models.DateField()

    class Meta:
        db_table = "persons"

    def mz_generation_status(self):
        import datetime
        if self.birth_date > datetime.date(1995, 1, 1):
            return "z 세대 입니다."
        elif self.birth_date > datetime.date(1981, 1, 1):
            return "x 세대 입니다."
        else:
            return "그 이전 세대 입니다."
            
    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    
    def save(self, *args, **kwargs):
        if self.pk == 1:
            return "save 되지 않습니다." 
        else:
            super().save(*args, **kwargs)  # 실제 save() 를 호출 
        
    def delete(self, *args, **kwargs):
        print(self.full_name)
        self.mz_generation_status() 
        super().delete(*args, **kwargs)



"""
get_필드_display() choice인자를 갖는 필드가 있으면, 설명 문자열을 반환한다.
아래의 경우 해당 객체가 S라면 Small을 반환하는 것이다. 
"""

class PersonChoice(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name        = models.CharField(max_length=60)
    shirt_size  = models.CharField(max_length=1, choices=SHIRT_SIZES)

    class Meta:
        db_table = "personchoice"
    
    def save(self, *args, **kwargs):
        # user.save() 할때 호출되는 내장함수 Overide
        # self.pk 는 생성되고 나서 생기기에, 
        if not self.pk:
            # on Create
            if self.shirt_size not in ["S", "M", "L"]:
                self.shirt_size = "S" 

        # else:
		# 	# on Update
        #     do_something()
        return super(PersonChoice, self).save(*args, **kwargs)
