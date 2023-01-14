 
from django.urls import path
from .import views
from knox import views as knox_views
from .views import RegistrationAPI,LoginAPI,UserAPI,RecordMeal
from knox import views as knox_views
urlpatterns = [
 
path('login/', LoginAPI.as_view(), name='knox_logout'),
path('recordmeal/', views.RecordMeal.as_view()),
path('calory_status', views.calory_status, name="calory_status"),

path('food_store_by_user', views.food_store_by_user, name="food_store_by_user"),
path('activity_store_by_user', views.activity_store_by_user, name="activity_store_by_user"),
path('register/', RegistrationAPI.as_view()),
path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
path('user/', UserAPI.as_view()),
]