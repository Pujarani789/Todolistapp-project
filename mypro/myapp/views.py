from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone

#**************Read********************

class ListTodo(generics.ListAPIView):
    queryset = Todoapp.objects.all()
    serializer_class = ToDoappSerializer

#*************Update******************
   
class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = Todoapp.objects.all()
    serializer_class = ToDoappSerializer

#**************Create******************    
class CreateTodo(generics.CreateAPIView):
    queryset = Todoapp.objects.all()
    serializer_class = ToDoappSerializer
    
    

#***************Delete*****************
class DeleteTodo(generics.DestroyAPIView):
    queryset = Todoapp.objects.all()
    serializer_class = ToDoappSerializer



class TaskDueTodayView(APIView):
    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        tasks = Todoapp.objects.filter(due_date=today)
        serializer = ToDoappSerializer(tasks, many=True)
        return Response(serializer.data)