from rest_framework import serializers
from .models import *

class ToDoappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todoapp
        fields = ('id','Title','description','due_date','completed')
        
        
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_due_date(self, value):
        if value and value < timezone.now().date():
            raise serializers.ValidationError("Due date must be a future date.")
        return value
