from django.contrib import admin
from django.urls import path

from core.vehicles.views import index, crudList, categoryCreate, categoryDelete, categoryUpdate

urlpatterns = [
    path('',index,name='index'),
    path('crud',crudList,name='crud_list'),
    path('categoryCreate',categoryCreate,name='crud_create'),
    path('categoryDelete/<int:id>/',categoryDelete,name='crud_delete'),
    path('categoryUpdate/<int:id>/',categoryUpdate, name='crud_update'),
]
