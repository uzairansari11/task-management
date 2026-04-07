from rest_framework.views import APIView
from tasks.models import Task
from tasks.serializers import TaskReadSerializer, TaskWriteSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class TaskCreateListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        queryset = Task.objects.select_related(
            'assigned_to', 'created_by').filter(created_by=request.user)

        serializer = TaskReadSerializer(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        #   pass
        created_by = request.user.id
        request.data['created_by'] = created_by
        serializer = TaskWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
