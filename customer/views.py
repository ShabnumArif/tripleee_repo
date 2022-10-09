from django.shortcuts import render

# Create your views here.

def artists_list(request):
     return render(request,'customer_templates/artists_list.html')
def categories(request):
     return render(request,'customer_templates/categories.html')
def homepage(request):
     return render(request,'customer_templates/homepage.html')
def payment_page(request):
     return render(request,'customer_templates/payment_page.html')
def product(request):
     return render(request,'customer_templates/product.html')
def seller_name_product_price(request):
     return render(request,'customer_templates/seller_name_product_price.html')
