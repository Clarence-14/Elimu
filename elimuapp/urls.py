
from django.contrib import admin
from django.urls import path
from elimuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('gallery/', views.gallery),
    path('info/', views.information),
    path('table/', views.table)

]
