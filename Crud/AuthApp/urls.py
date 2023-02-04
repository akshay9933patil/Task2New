from django.urls import path
from .views import UserRegisterAPI


urlpatterns = [
    path('user/', UserRegisterAPI.as_view()),
]