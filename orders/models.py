from django.db import models

# Create your models here.

from customers.models import Customer
from products.models import Product  # Assuming you have a Product model

class Order(models.Model):
    # Deletion status choices
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = (
        (LIVE, 'Live'),
        (DELETE, 'Delete'),
    )

    # Order status choices
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4

    STATUS_CHOICE = (
        (CART_STAGE, "CART_STAGE"),
        (ORDER_CONFIRMED, "ORDER_CONFIRMED"),
        (ORDER_PROCESSED, "ORDER_PROCESSED"),
        (ORDER_DELIVERED, "ORDER_DELIVERED"),
        (ORDER_REJECTED, "ORDER_REJECTED"),
    )

    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name="orders", null=True)
    order_status = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} by {self.owner}"


class OrderedItem(models.Model):
    product = models.ForeignKey(Product, related_name='ordered_items', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.quantity}x {self.product.name} in Order #{self.order.id}"
