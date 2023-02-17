from django.db import models
from django.contrib.auth.models import User

# Create your models here.
todos=[

    {"id":1,"task_name":"gbillpay","user":"ram"},
    {"id":2,"task_name":"task2","user":"ravi"},
    {"id":3,"task_name":"task3","user":"arjun"},
    {"id":4,"task_name":"task4","user":"aravind"},
    {"id":5,"task_name":"task5","user":"arjun"},
    {"id":6,"task_name":"task6","user":"hari"},

    
]

class Todos(models.Model):
    task_name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
   

# orm query for creating an object

# ModelName.objects.create(field1=value1,field2=value2,,,,,fieldn=valuen)
# Todos.objects.create(task_name="ebill",user="ram")


# orm query for fetching all records

# qs=Modename.objects.all()
# qs=Todos.objects.all()

# filtering

# qs=modelname.objects.filter(user="alam")

# update orm

# Todos.objects.filter(id=1).update(task_name=:"e bill")