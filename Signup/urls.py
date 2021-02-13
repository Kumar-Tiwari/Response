from django.urls import path
from .views import Signup_View

urlpatterns = [
    path('create', Signup_View,name="signup"),
]