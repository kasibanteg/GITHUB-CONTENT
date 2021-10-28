from django.db import models


# Create your models here.

class Category(models.Model):
    categoryName = models.CharField(max_length=100)


class Product(models.Model):
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productBrand = models.CharField(max_length=100)