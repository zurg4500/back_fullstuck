from django.db.models.signals import pre_save
from django.dispatch import receiver
from slugify import slugify

from .models import Product

@receiver(pre_save, sender=Product)
def get_pre_save(sender, instance: Product, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
    instance.in_stock = instance.quantity > 0

