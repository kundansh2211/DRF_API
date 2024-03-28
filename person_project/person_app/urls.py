from django.urls import path
from .views import PersonAPI

urlpatterns = [
    path('person/', PersonAPI.as_view()),
    path('person/<int:pk>', PersonAPI.as_view())
]  