from django.db import models

class Books(models.Model):
    Title=models.CharField(max_length=200)
    Author=models.CharField(max_length=30)
    ISBN=models.CharField(max_length=40)
    
    def __str__(self):
        return self.Title