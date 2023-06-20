from slugify import slugify
from utils.utils import now
from .tasks import notify_about_new_product


def get_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title) + now()
    instance.in_stock = instance.quantity > 0


def product_post_save(sender, instance, *args, **kwargs):
    notify_about_new_product.delay()
