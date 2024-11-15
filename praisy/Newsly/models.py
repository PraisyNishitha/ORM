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
