from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.make_logout, name="logout"),
    path('login/', views.make_login, name="login")
]