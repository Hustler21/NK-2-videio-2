from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import *
from django.db.models import Q
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
            single_product = Product.objects.get(slug=prod_slug)
            product_gallery = ProductGallery.objects.filter(product_id=single_product.id)
            context= {'products':products,'product_gallery':product_gallery}
       else:
            messages.warning(request,"Product not found")
            return redirect('home')
    else:
        messages.warning(request,"Category not found")
        return redirect('collections')
    return render(request,'store/view.html',context)
    

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product = Product.objects.order_by('-created_at').filter(Q(description__icontains=keyword) | Q(name__icontains=keyword))
    
            context = {
                'product': product,
             
            }
            return render(request, 'store/searchresult.html', context)
    
    # If no keyword provided or keyword is empty, redirect to the same page.
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
