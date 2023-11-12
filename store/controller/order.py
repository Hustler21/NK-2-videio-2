from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from store.models import Order,Cart, OrderItem, Product, Profile


@login_required(login_url='loginpage')

def index(request):
    orders =Order.objects.filter(user=request.user).order_by('-created_at')
    context = {'orders':orders}
    return render(request, 'store/orders.html',context)

@login_required(login_url='loginpage')
def vieworder(request, t_no):
    try:
        order = Order.objects.get(tracking_ID=t_no, user=request.user)
        orderitems = OrderItem.objects.filter(order=order)

        context = {'order': order, 'orderitems': orderitems}
        return render(request, 'store/vieworders.html', context)
    except ObjectDoesNotExist:
        # Handle the case where no order with the given tracking_ID and user is found
        return HttpResponse("Order not found or you don't have permission to view this order.", status=404)