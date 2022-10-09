from django.urls import path
from . import views
urlpatterns=[
    path('approval',views.approval),
    path('reviews_block',views.reviews_block),
    path('sales_report',views.sales_report),
    path('search_artist',views.search_artist),
]
