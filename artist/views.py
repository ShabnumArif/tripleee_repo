from django.shortcuts import render

# Create your views here.
def add_product(request):
     return render(request,'artist_templates/add_product.html')
def catalogue(request):
     return render(request,'artist_templates/catalogue.html')
def change_password(request):
     return render(request,'artist_templates/change_password.html')
def images(request):
     return render(request,'artist_templates/images.html')
def rate(request):
     return render(request,'artist_templates/rate.html')
def stock_update(request):
     return render(request,'artist_templates/stock_update.html')
def view_orders(request):
     return render(request,'artist_templates/view_orders.html')
