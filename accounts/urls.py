from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),

    path('products/', views.products, name="products"),
    path('createproduct/', views.createProduct, name="create_product"),
    path('view_product/<str:pk>/', views.viewProduct, name="view_product"),
    path('update_product/<str:pk>/', views.updateProduct, name="update_product"),
    path('delete_product/<str:pk>/', views.deleteProduct, name="delete_product"),

    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings, name="account"),

    path('customers/', views.customers, name="customers"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('create_customer/', views.createCustomer, name="create_customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('view_order/<str:pk>/', views.viewOrder, name="view_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


    path('employs/', views.employs, name='employs'),

    path('create_cuttingmaster/', views.createCuttingmaster, name='create_cuttingmaster'),
    path('cuttingmaster/<str:pk_cutting>/', views.cuttingmaster, name="cuttingmaster"),
    path('delete_cuttingmaster/<str:pk_cutting>/', views.deleteCuttingmaster, name="delete_cuttingmaster"),

    path('create_sewingmaster/', views.createSewingmaster, name='create_sewingmaster'),
    path('sewingmaster/<str:pk_sewing>/', views.sewingmaster, name="sewingmaster"),
    path('delete_sewingmaster/<str:pk_sewing>/', views.deleteSewingmaster, name="delete_sewingmaster"),

    path('create_subemploy/', views.createSubemploy, name='create_subemploy'),
    path('subemploy/<str:pk_subem>/', views.subemploy, name="subemploy"),
    path('delete_subemploy/<str:pk_subem>/', views.deleteSubemploy, name="delete_subemploy"),

]