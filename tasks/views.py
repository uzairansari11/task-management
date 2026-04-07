from rest_framework.views import APIView
from tasks.models import Task
from tasks.serializers import TaskReadSerializer, TaskWriteSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.template.context_processors import request
from rest_framework import status


class TaskCreateListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        queryset = Task.objects.select_related(
            'assigned_to', 'created_by').filter(created_by=request.user)

        serializer = TaskReadSerializer(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task=serializer.save(created_by = request.user)

        return Response(data=TaskReadSerializer(task).data, status=status.HTTP_201_CREATED)


class TaskDetailAPIView(APIView):
    
    def get_object(self,pk,user):
        return get_object_or_404(
            Task.objects.select_related("created_by","assigned_to").filter(created_by=user),
            id=pk
        )
    
    def get(self,request,pk):
        instance = self.get_object(
          
            pk,request.user
        )
        serializer=TaskReadSerializer(instance)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def patch(self,request,pk):
        instance = self.get_object(
          
            pk,request.user
        )
        serializer=TaskWriteSerializer(instance,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
            
        task = serializer.save()
        response_data = TaskReadSerializer(task)
        
        return Response(data=response_data.data,status=status.HTTP_200_OK)
    
    def delete(self,request,pk):
        instance = self.get_object(
          
            pk,request.user
        )
       
        instance.delete()
        
        return Response(data=TaskReadSerializer(instance).data,status=status.HTTP_204_NO_CONTENT)
    



class AssignedAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        task_status = request.query_params.get("status",None)
        priority = request.query_params.get("priority",None)
        
        queryset = Task.objects.select_related("assigned_to","created_by").filter(
            assigned_to=request.user,
        )
        
        if task_status:
            queryset=queryset.filter(status=task_status)
        if priority :
            queryset=queryset.filter(priority=priority)
        queryset=queryset.order_by("-created_at")
        
        serializer=TaskReadSerializer(queryset,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)