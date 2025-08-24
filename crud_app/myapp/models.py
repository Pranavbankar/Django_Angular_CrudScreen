from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    dob = models.DateField()
    is_active = models.BooleanField()


    def __str__(self):
        return self.name



