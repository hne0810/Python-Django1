from django.db import models

# Create your models here.
class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    
class Major(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    id_sub = models.ForeignKey('Subject', on_delete=models.RESTRICT, null=True, blank=True)
    def __str__(self):
        return self.name
    

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    sex = models.BooleanField()
    birth_year = models.IntegerField(),
    id_major = models.ForeignKey('Major', on_delete=models.RESTRICT, null=True, blank=True)
    def __str__(self):
        return self.name