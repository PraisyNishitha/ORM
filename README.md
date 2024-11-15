# Ex02 Django ORM Web Application
## Date: 13/11/24

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Customer,CustomerAdmin
admin.site.register(Customer,CustomerAdmin)

models.py

from django.db import models
from django.contrib import admin
class Customer(models.Model):
     Name=models.CharField(max_length=10)
     Accno=models.IntegerField(primary_key="accno")
     Email=models.EmailField()
     Dob=models.DateField()
     Adharno=models.IntegerField()

class CustomerAdmin(admin.ModelAdmin):
     list_display=('Name','Accno','Email','Dob','Adharno')

```


## OUTPUT
![alt text](<Screenshot (10).png>)
![alt text](<Screenshot 2024-11-16 024121.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
