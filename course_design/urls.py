from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('target/', views.target, name='target'),
    path('course/', views.course, name='course'),
    path('verifycode/', views.verifycode, name='verifycode'),

]
