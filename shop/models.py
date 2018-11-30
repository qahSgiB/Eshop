from django.db import models
from django.contrib.postgres.fields import ArrayField



class Product(models.Model):
    name = models.CharField(max_length=50)

class ProductX(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    style = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sizes = ArrayField(models.DecimalField(max_digits=3, decimal_places=1))
    image = models.ImageField(upload_to='shop/images')

class ProductXDetailImage(models.Model):
    image = models.ImageField(upload_to='shop/images')
    productX = models.ForeignKey(ProductX, on_delete=models.CASCADE)

class MainInfo(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
