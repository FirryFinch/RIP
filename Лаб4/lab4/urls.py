from django.contrib import admin
from django.urls import path
from lab4_app import views
urlpatterns = [
 path('admin/', admin.site.urls),
 path('', views.btfmovies, name='main_url'),
 path('btfmovie/<int:id>', views.btfmovie, name='btfmovie_url'),
]
