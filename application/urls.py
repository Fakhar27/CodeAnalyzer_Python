from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('',views.fileuplaoding,name='fileuplaoding'),
    path('', views.analyze_code_view, name='analyze_code_view'),
    path('result/', views.result, name='result'),
]