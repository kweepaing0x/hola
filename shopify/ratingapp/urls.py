from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index , name="index"),
    path('user_name', views.ask_name , name='usern'),
    path('first_product',views.first_page, name="fpage"),
    path('second_product', views.second_page, name='spage'),
    path('third_product', views.third_page, name="tpage"),
    path('congrats',views.end_page, name="epage"),
]