from adminuser import serializers
from rest_framework import serializers
from .models import Foods
from .models import Assesment

from .models import Activity
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class FoodsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    calory = serializers.IntegerField(required=False, default=0)
    carbs = serializers.IntegerField(required=False, default=0)

    fat = serializers.IntegerField(required=False, default=0)

    protein = serializers.IntegerField(required=False, default=0)
    class Meta:
        model = Foods
        fields = ["name", "calory", "carbs", "fat", "protein"]
    

class ActivitySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    calory_per_hr = serializers.IntegerField(required=False, default=0)
 
     
    class Meta:
        model = Activity
        fields = ["name", "calory_per_hr"]

    
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")

    
class MealSerializer(serializers.ModelSerializer):
    foodname_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=0)
    username_id = serializers.IntegerField(default=0)
    calory_burnout = serializers.IntegerField( default=0)
    activity_id = serializers.IntegerField()
    timespend = serializers.IntegerField(default=0)
    asses_date=serializers.DateTimeField()
    class Meta:
        model = Assesment
        fields = ["activity_id", "timespend","foodname_id", "quantity", "username_id","calory_burnout","asses_date"] 

    