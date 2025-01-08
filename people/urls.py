from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_list, name='people_list'),
    path('new/', views.people_new, name='people_new'),
    path('edit/<int:id>', views.people_edit, name='people_edit'),
    path('delete/<int:id>', views.people_delete, name='people_delete'),
]