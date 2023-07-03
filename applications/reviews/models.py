from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class AbstractedModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey('product.Product', on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Comment(AbstractedModel):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.id} from {self.user.username}"

    class Meta:
        default_related_name = 'comments'



class RatingChoises(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

 
class Rating(AbstractedModel):
    rate = models.PositiveIntegerField(choices=RatingChoises.choices)

    def __str__(self):
        return str(self.rate)
        
    class Meta:
        default_related_name = 'ratings'
        unique_together = ('user', 'product')


class Favorite(AbstractedModel):
    pass

    class Meta:
        default_related_name = 'favorites'
        unique_together = ('user', 'product')