from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    status = models.BooleanField()
    price = models.FloatField()
    createdby = models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_created')
    creation_date = models.DateTimeField()
    last_update_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_updated')
    last_update_date = models.DateTimeField()

    def __str__(self):
        return self.name
