"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shops.views import index,home,products,cart,add_to_cart,remove_from_cart,checkout,place_order
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('',home,name='home'),
    path('products/',products,name='products'),
    path('cart/',cart,name='cart'),
    path('cart/add/<int:product_id>/',add_to_cart,name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/',remove_from_cart,name='remove_from_cart'),
    path('checkout/',checkout,name='checkout'),
    path('place_order/',place_order,name='place_order'),
]