from django.db import models
from product.models import Product
from django.contrib.auth.models import User

class Useditems(models.Model):
    items = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='used_items')
    qty = models.IntegerField()
    createdby = models.ForeignKey(User,on_delete=models.CASCADE,related_name='invused_created')
    creation_date = models.DateTimeField()
    last_update_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='invused_updated')
    last_update_date = models.DateTimeField()

class Inventory(models.Model):
    prnum = models.CharField(max_length=300)
    items = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='inv_items')
    qty = models.IntegerField()
    createdby = models.ForeignKey(User,on_delete=models.CASCADE,related_name='inv_created')
    creation_date = models.DateTimeField()
    last_update_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='inv_updated')
    last_update_date = models.DateTimeField()


class DamageStock(models.Model):
    items = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='damage_items')
    qty = models.IntegerField()
    createdby = models.ForeignKey(User,on_delete=models.CASCADE,related_name='invdamage_created')
    creation_date = models.DateTimeField()
    last_update_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='invdamage_updated')
    last_update_date = models.DateTimeField()

