from .views import ListAPIProducts,ListAPICats
from django.urls import path

urlpatterns = [
    path('api/v1/', ListAPIProducts.as_view()),
    path('api/v2/', ListAPICats.as_view()),
]