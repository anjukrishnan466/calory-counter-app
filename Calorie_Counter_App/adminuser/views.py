from pstats import Stats
from urllib import request, response
from django.shortcuts import render
from .models import Foods
from .models import Activity
from django.http import HttpResponse
from rest_framework import response 
from rest_framework.decorators import api_view, renderer_classes
# from .serializers import FoodSerializer
# Create your views here.
from .serializers import FoodsSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .import serializers
from django.shortcuts import render, get_object_or_404
from .serializers import ActivitySerializer
from rest_framework import serializers

class FoodViews(APIView):
    def post(self, request):
        serializer = FoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
@api_view(('GET',))
def food_index(request):
    foods = Foods.objects.all().order_by('id')
    all_indexes = [] 
    for food in foods:
            food_list = {
                "foodname": food.name ,
                "calory": food.calory ,
                "carb": food.carbs ,
                "fat": food.fat ,
                "protein": food.protein ,
            }
            all_indexes.append(food_list)  
    return response.Response(all_indexes)
     
@api_view(['POST'])
def food_store(request):
    foods = FoodsSerializer(data=request.data)
    if Foods.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if foods.is_valid():
        foods.save(approve_by_admin=1)
        return Response(foods.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])  
def food_edit(request, pk):
    foods = Foods.objects.get(pk=pk)
    data = FoodsSerializer(instance=foods, data=request.data)
    if data.is_valid():
        data.save(approve_by_admin=1)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def food_delete(request, pk):
    foods = get_object_or_404(Foods, pk=pk)
    foods.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(('GET',))
def activity_index(request):
    activity = Activity.objects.all().order_by('id')
    all_indexes = [] 
    for act in activity:
            activity_list = {
                "activityname": act.name ,
                "calory_per_hr": act.calory_per_hr ,
               }
            all_indexes.append(activity_list)  
    return response.Response(all_indexes)
@api_view(['POST'])
def activity_store(request):
    activity = ActivitySerializer(data=request.data)
    print(activity)
    if Activity.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if activity.is_valid():
        activity.save(approve_by_admin=1)
        return Response(activity.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])  
def activity_edit(request, pk):
    activity = Activity.objects.get(pk=pk)
    data = ActivitySerializer(instance=activity, data=request.data)
    if data.is_valid():
        data.save(approve_by_admin=1)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def activity_delete(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    activity.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])  
def food_approve(request, pk):
    foods = Foods.objects.get(pk=pk)
    if foods:
        foods.approve_by_admin=1
        foods.save()
        return Response("approved")
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)      
@api_view(['POST'])  
def activity_approve(request, pk):
    activity = Activity.objects.get(pk=pk)
    if activity:
        activity.approve_by_admin=1
        activity.save()
        return Response("approved")
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
