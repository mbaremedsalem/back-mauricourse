from django.urls import path
from .views import *
urlpatterns = [
    ####----------login---------------#####
    path('login/', MytokenManager.as_view(), name='token_obtain_pair'),
    ####---------register-------------#####
    path('register/', RegisterAPI.as_view(), name='user-register'),
]