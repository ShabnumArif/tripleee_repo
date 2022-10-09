from django.urls import path
from . import views

urlpatterns=[
    path('add_product',views.add_product),
    path('catalogue',views.catalogue),
    path('change_password',views.change_password),
    path('images',views.images),
    path('rate',views.rate),
    path('stock_update',views.stock_update),
    path('view_orders',views.view_orders)
]