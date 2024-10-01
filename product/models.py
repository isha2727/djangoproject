from django.db import models

class Banner(models.Model):
    banner = models.ImageField(upload_to="banner")

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to="products/images",null=True)

    def __str__(self) -> str:
        return self.name