from django.urls import path
from .views import *

urlpatterns = [
    path('', TodoListViewSet.as_view({'get': 'list'})),
    path('/best', BestViesSet.as_view({'get': 'list'}))
]
