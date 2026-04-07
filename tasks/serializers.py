from django.contrib.auth import get_user_model
from rest_framework import serializers
from tasks.models import Task
User = get_user_model()


class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TaskWriteSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status',
                  'priority', 'due_date', 'assigned_to','created_by']


class TaskReadSerializer(serializers.ModelSerializer):
    created_by = UserMiniSerializer(read_only=True)
    assigned_to = UserMiniSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority',
                  'due_date', 'created_by', 'assigned_to', 'created_at', 'updated_at']
