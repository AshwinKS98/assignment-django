from django.db import models

class YourModel(models.Model):  
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Rectangle(models.Model): 
    length = models.FloatField()
    width = models.FloatField()

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"