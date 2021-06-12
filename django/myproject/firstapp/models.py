from django.db import models

# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    fees =models.IntegerField()
    gender = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

        
class Data(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    fees =models.IntegerField(max_length=5)
    number=models.CharField(max_length=10)
    gender = models.CharField(max_length=5)




    def __str__(self):
        return self.fname
