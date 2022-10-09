from django.urls import path
from . import views
urlpatterns=[
    path('artists_list',views.artists_list),
    path('categories',views.categories),
    path('homepage',views.homepage),
    path('payment_page',views.payment_page),
    path('product',views.product),
    path('seller_name_product_price',views.seller_name_product_price),
]
