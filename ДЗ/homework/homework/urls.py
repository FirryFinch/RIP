"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('report/', views.report),
    path('create_movie/', views.create_movie),
    path('create_platform/', views.create_platform),
    path('report/edit_movie/<int:id>/', views.edit_movie),
    path('report/edit_platform/<int:id>/', views.edit_platform),
    path('report/delete_movie/<int:id>/', views.delete_movie),
    path('report/delete_platform/<int:id>/', views.delete_platform),
]