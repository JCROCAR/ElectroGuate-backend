from django.db import models
from users.models import User
from products.models import Product
from orders.models import Order
from django.utils import timezone
from django.dispatch import receiver
from utils.models.base import BaseModel
from django.db.models.signals import post_save

# Create your models here.

class Payment(BaseModel):
    """
    Model for 'Payments'
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    str_card_number = models.CharField(max_length=16, null=False, blank=False)
    str_name = models.CharField(max_length=45, null=False, blank=False)
    card_date = models.DateTimeField(null=False, default=timezone.now)


