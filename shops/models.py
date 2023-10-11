from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.pk}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
