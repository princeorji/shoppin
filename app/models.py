from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField()
    price = models.DecimalField(max_digits=9,decimal_places=2 )
    date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_id = ShortUUIDField()
    complete = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return str(self.id)

