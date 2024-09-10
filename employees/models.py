from django.db import models

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    dob = models.DateField(null=True, blank=True)
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    
   

    def __str__(self):
        return self.name
