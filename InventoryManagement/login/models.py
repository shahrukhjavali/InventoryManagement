from django.db import models
from django.contrib.auth.models import User

class UserRole(models.Model):
    roles = (
        ('SE','sale executive'),
        ('IM','inventory Manager'),
        ('PM','Purchase Manager'),
        ('Sup','Supplier'),
        ('AD','Admin'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=30,choices=roles)

    def __str__(self):
        return self.role

