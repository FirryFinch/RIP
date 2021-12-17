from django.contrib import admin
from django.urls import path
from lab4_app import views
urlpatterns = [
 path('admin/', admin.site.urls),
 path('', views.engines, name='main_url'),
 path('engine/<int:id>', views.engine, name='engine_url'),
]
