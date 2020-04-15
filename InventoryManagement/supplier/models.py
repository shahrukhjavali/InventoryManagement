from django.db import models
from login.models import UserRole
from product.models import Product
from django.contrib.auth.models import User

class Supplier(models.Model):
    supplier = models.ForeignKey(UserRole,on_delete=models.CASCADE,related_name='supplier_name')
    mobnum = models.CharField(max_length=10)
    Adderss = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    email = models.EmailField()
    status = models.BooleanField()
    #products = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='products_supp')
    createdby = models.ForeignKey(User,on_delete=models.CASCADE,related_name='supplier_created')
    creation_date = models.DateTimeField()
    last_update_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='supplier_updated')
    last_update_date = models.DateTimeField()


    def __str__(self):
        return self.supplier.user