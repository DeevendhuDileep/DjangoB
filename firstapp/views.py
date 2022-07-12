from django.shortcuts import render

# Create your views here.

def load_home_page(request):
    return render(request,'home.html')

def load_index_page(request):
    return render(request,'index.html')