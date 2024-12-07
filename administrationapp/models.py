from django.db import models

# Create your models here.


from django.db import models

class PatientList(models.Model):
    Register_Number = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    Date = models.DateField()  # Changed to DateField for storing date
    Reason = models.CharField(max_length=100)

    def __str__(self):
        return self.Register_Number

from django.db import models

class Staff(models.Model):
    username = models.CharField(max_length=4, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.username