from django.db import models
from django.urls import reverse

# Create your models here.

class School(models.Model):
    scname = models.CharField(max_length=100)
    scprincipal = models.CharField(max_length=100)
    sclocation = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.scname
    
    def get_adsolutre_url(self):
        return reverse('SchoolDetail',kwargs={'pk':self.pk})
    
class Student(models.Model):
    sname = models.CharField(max_length=100)
    sage = models.CharField(max_length=100)
    scname = models.ForeignKey(School,on_delete=models.CASCADE,related_name='jay')

    def __str__(self) -> str:
        return self.sname