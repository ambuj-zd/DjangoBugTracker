from django.db import models
# Create your models here.

class User(models.Model):
    userid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=150)
    

    def __str__(self):
        return self.name
    
class Task(models.Model):
    userid = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    status = models.CharField(max_length=100)
    details = models.TextField(max_length=150)
    tasknum = models.IntegerField()
    
    
    def __str__(self):
        return self.title
    
class Role(models.Model):
    name = models.ForeignKey(User,null=True, on_delete=models.CASCADE) 
    role = models.CharField(max_length=70)
    
    
    