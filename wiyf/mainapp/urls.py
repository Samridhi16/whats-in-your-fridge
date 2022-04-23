from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('add/', views.add,name="add"),
    path('add/create', views.create,name="update"),
    path('cook/', views.cook,name="cook"),
    path('cook/recom', views.recommendations,name="recom"),

]
