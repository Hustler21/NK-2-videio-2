from django.db import models
from django.contrib.auth.models import User
import datetime
import os


def get_file_path(request,filename):
    orginal_filename =filename
    nowTime =datetime.datetime.now().strftime('%Y%m%d%H:%M%S')
    filename ="%s%s" %(nowTime,orginal_filename)
    return os.path.join('uploads/',filename)

class Category(models.Model):
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False,help_text="0-default,1-hidden")
    trending = models.BooleanField(default=False,help_text="0-default,1-trending")
    meta_title = models.CharField(max_length=150,null=False,blank=False)
    meta_keyword = models.CharField(max_length=500,null=False,blank=False)
    meta_description = models.CharField(max_length=500,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to=get_file_path,null=True,blank=True)
    small_description = models.TextField(max_length=500, null=False, blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    orginal_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False,help_text="0-default,1-hidden")
    trending = models.BooleanField(default=False,help_text="0-default,1-trending")
    tag = models.CharField(max_length=150,null=False,blank=False)
    meta_title= models.CharField(max_length=150,null=False,blank=False)
    meta_keyword = models.CharField(max_length=500,null=False,blank=False)
    meta_description = models.CharField(max_length=500,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    created_qty = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=150,null=False,blank=False)
    lname = models.CharField(max_length=150,null=False,blank=False)
    email = models.CharField(max_length=150,null=False,blank=False)
    phone = models.CharField(max_length=150,null=False,blank=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150,null=False,blank=False)
    state = models.CharField(max_length=150,null=False,blank=False)
    country = models.CharField(max_length=150,null=False,blank=False)
    pincode = models.CharField(max_length=150,null=False,blank=False)
    total_price = models.FloatField(null=False)
    payment_mode =models.CharField( max_length=150,null=False)
    payment_id = models.CharField( max_length=250,null=True)
    orderstatuses ={
        ('Pending','Pending'),
        ('Out for Shipping','Out for Shipping'),
        ('Completed','Completed'),
    }
    status = models.CharField(max_length=150,choices=orderstatuses, default='Pending')
    message = models.TextField(null=True)
    tracking_ID = models.CharField(max_length=150,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id,self.tracking_ID)
    

class OrderItem(models.Model):
   order = models.ForeignKey(Order,on_delete=models.CASCADE)
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   price = models.FloatField(null=False)
   quantity = models.IntegerField(null=False)
   name= models.TextField(null=False,default=False)
   address = models.TextField(null=False,default=False)
   pincode = models.TextField(null=False,default=False)

   def __str__(self):
       return '{} - {}'.format(self.order.id,self.order.tracking_ID)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=50,null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150,null=False,blank=False)
    state = models.CharField(max_length=150,null=False,blank=False)
    country = models.CharField(max_length=150,null=False,blank=False)
    pincode = models.CharField(max_length=150,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
