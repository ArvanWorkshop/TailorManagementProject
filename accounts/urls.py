from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


    path('employs/', views.employs, name='employs'),
    path('cuttingmaster/<str:pk_cutting>/', views.cuttingmaster, name="cuttingmaster"),
    path('sewingmaster/<str:pk_sewing>/', views.sewingmaster, name="sewingmaster"),
    path('subemploy/<str:pk_subem>/', views.subemploy, name="subemploy"),


]