from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_due_date(value):
    if value < timezone.now().date():
        raise ValidationError('Due date must be a future date.')



class Todoapp(models.Model):
    Title = models.CharField(max_length=100)
    description=models.TextField(blank=True)
    completed=models.BooleanField(default=False)
    due_date=models.DateField(blank=False)
    
    def __str__(self):
        return self.Title
    
    
    
    

