from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

#Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title =models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name ="notes"
        verbose_name_plural = "notes"
        
class Homework(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description= models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title+' {}'.format(self.pk)
    
class Todo(models.Model):
    user = models.ForeignKey(User,on_delete =models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)
     
    def __str__(self):
            return self.title
    
    
USER_TYPE=(

    ("1", "teacher"),
    ("2", "student"),

)

class ModifiedUser(models.Model):
        user_type = models.CharField(max_length=100, choices=USER_TYPE)
    
        def __str__(self):
            return self.user_type