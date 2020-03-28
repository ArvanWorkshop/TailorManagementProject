from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings, name="account"),

    path('customer/<str:pk_test>/', views.customer, name="customer"),


    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('view_order/<str:pk>/', views.viewOrder, name="view_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


    path('employs/', views.employs, name='employs'),
    path('cuttingmaster/<str:pk_cutting>/', views.cuttingmaster, name="cuttingmaster"),
    path('sewingmaster/<str:pk_sewing>/', views.sewingmaster, name="sewingmaster"),
    path('subemploy/<str:pk_subem>/', views.subemploy, name="subemploy"),


]