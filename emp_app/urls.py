from django.urls import path
from . import views

urlpatterns=[
    path('', views.home,name='home'),
    path('createEmp/', views.createEmployee,name='createEmp'),
    path('createDep/', views.createDepartment,name='createDep'),
    path('createRole/', views.createRole,name='createRole'),
    path('update/<str:pk>/', views.update,name='update'),
    path('delete/<str:pk>/', views.delete,name='delete'),
    
    
    
]
