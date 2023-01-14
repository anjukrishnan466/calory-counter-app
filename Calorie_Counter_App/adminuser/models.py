from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Foods(models.Model):

    name = models.CharField(max_length=1250,unique=True)
    calory = models.IntegerField(default=0, null=True)
    carbs = models.IntegerField(default=0, null=True)
    fat = models.IntegerField(default=0, null=True)
    protein = models.IntegerField(default=0, null=True)
    approve_by_admin = models.IntegerField(default=0, null=False)

    image = models.FileField(
        upload_to="food/", max_length=250, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Activity(models.Model):

    name = models.CharField(max_length=1250,unique=True)
    calory_per_hr = models.IntegerField(default=0, null=True)
    approve_by_admin = models.IntegerField(default=0, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Assesment(models.Model):

    username = models.ForeignKey(User, on_delete=models.CASCADE)
    foodname = models.ForeignKey(Foods, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    timespend = models.IntegerField(null=True)
    calory_burnout = models.IntegerField(default=0, null=True)
    asses_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
