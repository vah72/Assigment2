from django.urls import path
from .views import *

app_name = 'todo'
urlpatterns = [
    path('listView/', listView, name='listView'),
    path('addlist/', listadd, name='listadd'),
    path('deletelist/<int:list_id>/', deletelist)
]