# Generated by Django 2.2.5 on 2020-04-12 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200411_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrole',
            name='role',
            field=models.CharField(choices=[('SE', 'sale executive'), ('IM', 'inventory Manager'), ('PM', 'Purchase Manager'), ('Sup', 'Supplier'), ('AD', 'Admin')], max_length=30),
        ),
    ]
