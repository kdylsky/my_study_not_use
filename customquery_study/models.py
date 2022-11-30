from django.db import models

class AccountQuerySet(models.QuerySet):
    def get_men_gender(self):
        return self.filter(gender="M")

    def get_women_gender(self):
        return self.filter(gender="W")

    def set_generation(self, age):
        generation=""
        if age >= 40:
            generation="40대"
        elif age >= 30:
            generation="30대"
        elif age >= 20:
            generation="20대"
        elif age >= 10:
            generation="10대"
        elif age >= 0:
            generation="0대"    
        return self.update(generation=generation)
        

class AccountManager(models.Manager):
    def get_queryset(self):
        return AccountQuerySet(self.model, using=self.db)

    def get_men_gender(self):
        return self.get_queryset().get_men_gender()

    def get_women_gender(self):
        return self.get_queryset().get_women_gender()

    def set_generation(self):
        return self.get_queryset().set_generation()


class AgeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(generation__icontains="30")


class Account(models.Model):
    GENDER=(
        ("M", "Men"),
        ("W", "Wonmen")
    )
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER, blank=True, default="W")
    generation = models.CharField(max_length=4, blank=True, default=" ")

    objects = AccountManager()
    objects = AccountQuerySet.as_manager()
    age_objects = AgeManager()

    class Meta:
        db_table = "accounts"

    def full_name(self):
        full_name = self.name + "성" 
        return full_name 
    