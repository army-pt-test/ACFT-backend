from django.db import models

# Create your models here.


class Cadet(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    middleinitial = models.CharField(max_length=1, null=True)
    gender = models.CharField(max_length=1, null=True)
    unit = models.CharField(max_length=100)
    date = models.DateField()
    mos = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    heightininches = models.CharField(max_length=2)
    weightinpounds = models.CharField(max_length=3)
    bodyfatpercentage = models.CharField(max_length=2)

    def __str__(self):
        return self.lastname
