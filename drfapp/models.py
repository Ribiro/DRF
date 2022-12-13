from django.db import models

# Create your models here.
class Students(models.Model): # should be class Student not class Students
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    description = models.TextField()
    date_enrolled = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name