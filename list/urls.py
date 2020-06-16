from django.urls import path
from .views import TodoListViewSet

urlpatterns = [
    path('', TodoListViewSet.as_view({'get': 'list'}))
]
