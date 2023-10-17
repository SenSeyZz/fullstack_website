from django.db import models

#python manage.py runserver

# Create your models here.
#------WHEN CREATING A NEW MODEL RUN : python manage.py makemigrations && python manage.py migrate ----------


#replace function with the imported algrotihms and use the variables here  

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    

    def __str__(self):
        """A string representation of the model."""
        return self.title
 
class Back(models.Model):
    number = models.CharField(max_length=200)
    description = models.TextField()
    

    def __str__(self):
        """A string representation of the model."""
        return self.number

