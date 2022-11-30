from django.urls import path
from . import views

urlpatterns = [
    path('', views.parser_home, name="parser_home"),
    path('create', views.create, name="create")
]