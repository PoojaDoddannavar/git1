from django.db import models

# Create your models here.
class Job(models.Model):
    Jobrole=models.CharField(max_length=30)
    Qualification=models.CharField(max_length=30)
    Specialisation=models.CharField(max_length=30)
    Location=models.CharField(max_length=30)
    Salary=models.IntegerField()
    ApplyDate=models.DateField()
    

