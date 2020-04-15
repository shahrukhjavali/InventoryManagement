from django.db import models
from django.contrib.auth.models import User
from supplier.models import Supplier
from product.models import Product
from master.models import Uom

class PurchaserOrder(models.Model):
    approvalstatus = (
        ('CR','Created'),
        ('AD','Approved'),
        ('RJ','Rejected'),
        ('HD','OnHold'),
    )
    prnumber = models.CharField(max_length=300)
    orderdate = models.DateTimeField()
    orderedby = models.ForeignKey(User,on_delete=models.CASCADE,related_name='order_by')
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,related_name='supplier_name')
    status = models.BooleanField()
    tax = models.IntegerField()
    Approval = models.CharField(max_length=30,choices=approvalstatus,default='Created')
    Approval_comments = models.CharField(max_length=250)


class PoItems(models.Model):
    po = models.ForeignKey(PurchaserOrder,on_delete=models.CASCADE,related_name='po_num')
    products = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product')
    quantity = models.IntegerField(default=1)
    uom = models.ForeignKey(Uom,on_delete=models.CASCADE,related_name='uom')
    total = models.FloatField()
    product_status = models.BooleanField()
    last_update_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='po_updated')
    last_update_date = models.DateTimeField() 

