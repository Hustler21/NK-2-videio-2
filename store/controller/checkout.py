import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


from store.models import Order,Cart, OrderItem, Product, Profile

@login_required(login_url='loginpage')
def index(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    cartitems = Cart.objects.filter(user=request.user)
    total_price =0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty

    userprofile = Profile.objects.filter(user=request.user).first()

    context ={'cartitems':cartitems,'total_price':total_price, 'userprofile':userprofile }
    return render(request,'store/checkout.html',context )


@login_required(login_url='loginpage')
def placeorder(request):
    if request.method =='POST':
        
        currentuser = User.objects.filter(id=request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name  =   request.POST.get('lname')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile =Profile()
            userprofile.user = request.user
            userprofile.phone    =   request.POST.get('phone')
            userprofile.address  =   request.POST.get('address')
            userprofile.city     =   request.POST.get('city')
            userprofile.state    =   request.POST.get('state')
            userprofile.country  =   request.POST.get('country')
            userprofile.pincode  =   request.POST.get('pincode')
            userprofile.save()

        neworder = Order()
        neworder.user = request.user
        neworder.fname    =   request.POST.get('fname') 
        neworder.lname    =   request.POST.get('lname')
        neworder.email    =   request.POST.get('email')
        neworder.phone    =   request.POST.get('phone')
        neworder.address  =   request.POST.get('address')
        neworder.city     =   request.POST.get('city')
        neworder.state    =   request.POST.get('state')
        neworder.country  =   request.POST.get('country')
        neworder.pincode  =   request.POST.get('pincode')

        neworder.payment_mode   = request.POST.get('payment_mode')
        neworder.payment_id   = request.POST.get('payment_id')

        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty
        neworder.total_price=cart_total_price

        trackno = neworder.fname+" "+neworder.lname+str(random.randint(11111,99999))
        while Order.objects.filter(tracking_ID=trackno) is None:
            trackno= neworder.fname+" "+neworder.lname+str(random.randint(11111,99999))
        neworder.tracking_ID= trackno
        neworder.save()
        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity = item.product_qty,
                address = neworder.address,
                pincode = neworder.pincode,
            )
            
        orderproduct =Product.objects.filter(id=item.product_id).first()
        orderproduct.quantity = orderproduct.quantity - item.product_qty
        orderproduct.save()
        

        #To clear user cart
        Cart.objects.filter(user=request.user).delete()
        messages.success(request,"Order placed Sucessfully")

        payMode = request.POST.get('payment_mode')

        if(payMode == "Paid with Razorpay"):
            mail_subject = 'Order placed Sucessfully'
            message = render_to_string('store/order_received_email.html', {
            'user': request.user,
            'neworderitems': neworderitems,})
            to_email = neworder.email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            return JsonResponse({'status': "Payment Completed successfully"})
            
        mail_subject = 'Order placed Sucessfully'
        message = render_to_string('store/order_received_email.html', {
        'user': request.user,
        'neworderitems': neworderitems,})
        to_email = neworder.email
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        send_email.send()
        
    return redirect('/')

@login_required(login_url='loginpage')
def razorpaycheck(request):
    cart = Cart.objects.filter(user=request.user)
    cart_total_price = 0
    for item in cart:
        cart_total_price = cart_total_price + item.product.selling_price * item.product_qty
    return JsonResponse({
        'cart_total_price': cart_total_price
    })

def orders(request):
    return HttpResponse("My orders page")