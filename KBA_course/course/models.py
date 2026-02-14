from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField()
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,
        related_name='course'
    )
    def __str__(self):
        return self.name