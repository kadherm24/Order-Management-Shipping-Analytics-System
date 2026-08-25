from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length= 100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.product_name