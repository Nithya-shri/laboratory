from django.db import models

# Create your models here.
class studentdetails(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    rollno=models.CharField(max_length=20)
    department=models.CharField(max_length=20)
    year=models.IntegerField()
    phoneno=models.IntegerField()
    hs=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    parent_phoneno=models.IntegerField()
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)

class maintooltable(models.Model):
    name=models.CharField(max_length=20,primary_key=True)
    subject=models.CharField(max_length=20)
    total_quantity=models.IntegerField()
    available_now=models.IntegerField()


class requestt(models.Model):
    
    
    name=models.ForeignKey(studentdetails,on_delete=models.CASCADE)
    toolname=models.ForeignKey(maintooltable,on_delete=models.CASCADE)
    tool=models.CharField(max_length=20)
    quantity_req=models.IntegerField()
    status=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)