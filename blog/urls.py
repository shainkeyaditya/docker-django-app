from django.urls import path
from . import views

urlpatterns = [
    path('', views.createBlog, name='blog')

]