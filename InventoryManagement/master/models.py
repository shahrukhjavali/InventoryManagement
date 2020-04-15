from django.db import models
from django.contrib.auth.models import User

class Uom(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)
    status = models.BooleanField()
    createdby = models.ForeignKey(User,on_delete=models.CASCADE,related_name='uomcreated')
    created_date = models.DateTimeField()
    last_update_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='uomupdated')
    last_update_date = models.DateTimeField()
