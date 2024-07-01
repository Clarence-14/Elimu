
from django.contrib import admin
from django.urls import path
from elimuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('info/', views.information, name='info'),
    path('table/', views.table, name='table'),
    path('form/', views.form, name='form'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),

]
