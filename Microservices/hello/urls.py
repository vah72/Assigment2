from django.urls import path
from .views import *

app_name = "hello"

urlpatterns = [
    path('', myView, name = 'myView'),
    path('dipto/',anotherHello ,name='anotherHello'),
]
