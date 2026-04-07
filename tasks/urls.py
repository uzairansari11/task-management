from django.urls import path

from tasks.views import TaskCreateListAPIView

urlpatterns = [
    
    path('',TaskCreateListAPIView.as_view(),name="task-create-list-view")
]