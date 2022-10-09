from django.shortcuts import render

# Create your views here.

def approval(request):
      return render(request,'admin_templates/approval.html')
def reviews_block(request):
     return render(request,'admin_templates/reviews_block.html')
def sales_report(request):
     return render(request,'admin_templates/sales_report.html')
def search_artist(request):
     return render(request,'admin_templates/search_artist.html')
