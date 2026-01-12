
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.deleteData , name='delete'),
    path('harddelete/<int:id>/', views.hardDelete , name='harddelete'),
    path('restore/<int:id>/', views.restore , name='restore'),
    path('sendemail/', views.sendEmail , name='sendEmail'),
]