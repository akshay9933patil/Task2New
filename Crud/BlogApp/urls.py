from django.urls import path
from .views import BlogCreateAPIView, BlogGenericView


urlpatterns = [
    path('blog/', BlogCreateAPIView.as_view()),
    path('blog/<int:pk>/', BlogGenericView.as_view()),
]