from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)

    def __str__(self):
        return self.name


class CuttingMaster(models.Model):
    CATEGORY = (
        ('daily', 'daily'),
        ('weekly', 'weekly'),
        ('monthly', 'monthly')
    )
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    selery_type = models.CharField(max_length=200, null=True, choices=CATEGORY)
    selery_amount = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    cuttingmaster_pic = models.ImageField(default="profile1.png", null=True, blank=True)

    def __str__(self):
        return self.name

class SewingMaster(models.Model):
    CATEGORY = (
        ('daily', 'daily'),
        ('weekly', 'weekly'),
        ('monthly', 'monthly')
    )
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    selery_type = models.CharField(max_length=200, null=True, choices=CATEGORY)
    selery_amount = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    sewingmaster_pic = models.ImageField(default="profile1.png", null=True, blank=True)

    def __str__(self):
        return self.name

class SubEmploy(models.Model):
    CATEGORY = (
        ('daily', 'daily'),
        ('weekly', 'weekly'),
        ('monthly', 'monthly')
    )
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    selery_type = models.CharField(max_length=200, null=True, choices=CATEGORY)
    selery_amount = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    subemploy_pic = models.ImageField(default="profile1.png", null=True, blank=True)

    def __str__(self):
        return self.name

#######################################################

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.TextField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    product_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

###########################################################

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('CuttingMaster', 'CuttingMaster'),
        ('SewingMaster', 'SewingMaster'),
        ('OtherEmploy', 'OtherEmploy'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        ('Complete Order','Complete Order')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    cuttingmaster = models.ForeignKey(CuttingMaster, null=True, on_delete=models.SET_NULL)
    sewingmaster = models.ForeignKey(SewingMaster, null=True, on_delete=models.SET_NULL)
    subemploy = models.ForeignKey(SubEmploy, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='Pending')
    note = models.CharField(max_length=1000, null=True, default='hello')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    delivery_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)


    def __str__(self):
        return self.product.name




