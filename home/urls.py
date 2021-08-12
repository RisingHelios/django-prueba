from django.urls import path
from . import views

urlpatterns = [
 path('',views.index, name='index'),
 path('estudiantes/<str:pk>/', views.estudiantes, name='estudiantes'),
]