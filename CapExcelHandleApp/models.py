from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.CharField(max_length=100)
    econtact = models.CharField(max_length=15)
    unique_id = models.IntegerField(max_length=10)
    class meta:
        db_table ="employee"