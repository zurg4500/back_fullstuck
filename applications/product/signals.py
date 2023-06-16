from slugify import slugify
from utils.utils import now


def get_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title) + now()
    instance.in_stock = instance.quantity > 0
