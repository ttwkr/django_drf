from django.shortcuts import render
from rest_framework import viewsets, generics, pagination, filters
from django.db import models
from .models import *
from .serializers import *
from django.http import JsonResponse, HttpResponse

# Create your views here.


class TodoListViewSet(viewsets.GenericViewSet):
    model = TodoList
    serializer_class = TodolistSerializer
    # 검색
    filter_backends = [filters.SearchFilter]
    search_fields = ["contents"]

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def list(self, request, *arg, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse({"result": serializer.data})


class BestViesSet(viewsets.GenericViewSet):
    model = Bests
    serializer_class = BestSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(todo__is_use=1)
        serializer = self.get_serializer(queryset, many=True)

        return JsonResponse({"result": serializer.data})


class ShopDetailViewSet(generics.RetrieveAPIView):
    model = Shop
    serializer_class = ShopDetailSerializer
    # 검색

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def retrieve(self, request, pk, *arg, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).get(id=pk)
        serializer = self.get_serializer(queryset)
        return JsonResponse({"result": serializer.data})


class MapShopListVeiwSet(viewsets.GenericViewSet):
    model = Shop
    serializer_class = MapShopListSerializer

    def queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(data=request.data)
        return JsonResponse({"result": serializer.data})


class LikeViewSet(generics.GenericAPIView):
    model = Likes
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        data = json.loads(json.dumps(request.data))
        serializer = self.serializer_class(data=data)

        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                return JsonResponse({"result": "success"})

            return JsonResponse({"result": "fail"})
        except Exception as ex:
            return JsonResponse({"result": str(ex)})

