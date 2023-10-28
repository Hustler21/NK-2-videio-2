from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'store/index.html')

def collections(request):
    category =Category.objects.filter(status=0)
    context ={
        'category':category
    }
    return render(request,'store/colllections.html',context)

def collectionsviews(request,slug):
    if(Category.objects.filter(status=0,slug=slug)):
        product = Product.objects.filter(category__slug=slug,status=0)
        category_name =Category.objects.filter(status=0).first()
        context ={'product':product,'category_name':category_name}
        return render(request,'store/product.html',context)
    else:
        messages.warning(request,"Category not found")
        return redirect('collections')
    
def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(status=0,slug=cate_slug)):
       if(Product.objects.filter(slug=prod_slug,status=0)):
            products = Product.objects.filter(slug=prod_slug,status=0).first
            context= {'products':products}
       else:
            messages.warning(request,"Product not found")
            return redirect('home')
    else:
        messages.warning(request,"Category not found")
        return redirect('collections')
    return render(request,'store/view.html',context)
    
    