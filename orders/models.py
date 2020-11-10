from django.db import models
from users.models import User
from products.models import Product
from django.dispatch import receiver
from utils.models.base import BaseModel
from django.db.models.signals import post_save

# Create your models here.

class Order(BaseModel):
    """
    Model for 'Orders'
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    str_deposit_number = models.CharField(max_length=12, null=False, blank=False)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    zip_code = models.CharField(max_length=6, null=False, blank=False)
    details = models.TextField(null=True, blank=True)


class DetailOrder(BaseModel):
    """
    Model for 'DetailOrder'
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)


# SIGNAL PARA AGREGAR DETALLE DE ORDEN A SU RESPECTIVA ORDEN, REALIZANDO EL CALCULO Y SUMANDO EL SUBTOTAL
@receiver(post_save, sender=DetailOrder)
def add_to_order(sender, instance=None, created=False, **kwargs):
    if created:
        subtotal =  instance.amount * instance.price
        order_target = Order.objects.get(id=instance.order.id)
        order_target.total = order_target.total + subtotal
        order_target.save()
    
