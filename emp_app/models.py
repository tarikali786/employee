from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Role(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=200)
    age=models.PositiveIntegerField(null=True,blank=True) 
    email=models.EmailField() 
    phone=models.IntegerField(null=True)
    address=models.CharField(max_length=500)
    image=models.ImageField(upload_to='project')
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(null=True)
    bonus=models.IntegerField(null=True)  
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    hire_date=models.DateField()
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['-updated']
        
    def __str__(self):
        return self.name