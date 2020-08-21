from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.create, name="create"),
    path('introduce/', views.introduce, name="introduce"),
    path('update/<int:designer_id>/', views.update, name="update"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('delete/<int:pk>', views.delete, name="delete"),
]