import datetime
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import serializers
from adminuser.serializers import UserSerializer,MealSerializer,FoodsSerializer,ActivitySerializer
from rest_framework import response 
from knox.views import LoginView as KnoxLoginView
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth.models import User, auth
from knox.models import AuthToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from adminuser.models import Assesment,Foods,Activity
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from adminuser.serializers import CreateUserSerializer, UserSerializer,LoginUserSerializer
# Register API
# class RegisterAPI(generics.CreateAPIView):
#   serializer_class = RegisterSerializer

# def post(self, request, *args, **kwargs): 
#     serializer = self.get_serializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.save()
    
#     return Response({
#  "user": UserSerializer(user, context=self.get_serializer_context()).data,
#  "token": AuthToken.objects.create(User)[1]
#  })
    
# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

# def post(self, request, format=None):
#     serializer = AuthTokenSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data['user']
#     login(request, user)
#     return super(LoginAPI, self).post(request, format=None)
    # return Response({
    #     "user": UserSerializer(user, context=self.get_serializer_context()).data,  # Get serialized User data
    #     "token": token
    # })
 
class RecordMeal(APIView):
    def post(self, request):
        serializer = MealSerializer(data=request.data)
        food_id=request.data['foodname_id']
        activity_id=request.data['activity_id']
        quantity=request.data['quantity']
        timespend=request.data['timespend']
        food=Foods.objects.get(id=food_id)
        activity=Activity.objects.get(id=activity_id)
        calory_activity=activity.calory_per_hr
        calory_burnout=timespend*calory_activity
        calory=food.calory
        calory_intake=calory*quantity
        total_calory_burnout=calory_intake-calory_burnout
        
        if serializer.is_valid():
            
            serializer.save(calory_burnout=total_calory_burnout)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(('GET',))

def calory_status(request):
    status = request.GET['status']
    cal_count=0
    total_time_spend=0
    if status=="daily":
        assesment = Assesment.objects.filter(username_id=121,asses_date=datetime.date.today()).all()
     
    elif status=="week":
        to_date=timezone.now()
        from_date=timezone.now() - timedelta(days=7)
        assesment = Assesment.objects.filter(username_id=121,asses_date__range=[from_date, to_date]).all()
       
 
    else:
        to_date=timezone.now()
        from_date=timezone.now() - timedelta(days=30)
        assesment = Assesment.objects.filter(username_id=121,asses_date__range=[from_date, to_date]).all()
       
    for asses in assesment:
        cal_count=asses.calory_burnout+cal_count
        total_time_spend=asses.timespend+total_time_spend
     
        
 
    total_cal_count=cal_count/total_time_spend
    calory = {
                "total_calory":cal_count ,
                "time_spend": total_time_spend ,
                "total_calory_burnout": total_cal_count
                 
            }
    return response.Response(calory)
@api_view(['POST'])
def food_store_by_user(request):
    foods = FoodsSerializer(data=request.data)
    if Foods.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if foods.is_valid():
        foods.save(approve_by_admin=0)
        return Response(foods.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def activity_store_by_user(request):
    activity = ActivitySerializer(data=request.data)
    print(activity)
    if Activity.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if activity.is_valid():
        activity.save(approve_by_admin=0)
        return Response(activity.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })