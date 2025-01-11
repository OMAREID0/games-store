from django.db import models
from api.users.models import User
from api.product.models import Product
# Create your models here.

class Order(models.Model):
    PENDING_STATE = "p"
    COMPLETED_STATE = "c"
    ORDER_CHOICES = ((PENDING_STATE, "pending"), (COMPLETED_STATE, "completed"))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=250, unique=True)
    status = models.CharField( max_length=1, choices=ORDER_CHOICES, default=PENDING_STATE)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.order_number}"





class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="order_items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product_order", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False)