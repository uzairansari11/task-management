from django.urls import path

from tasks.views import AssignedAPIView, TaskCreateListAPIView, TaskDetailAPIView

urlpatterns = [
    
    path('',TaskCreateListAPIView.as_view(),name="task-create-list-view"),
    path('<int:pk>/',    TaskDetailAPIView.as_view(),name="task-detail-view"),
    path('assigned/',AssignedAPIView.as_view(),name="task-create-list-view"),
    
    
    
]