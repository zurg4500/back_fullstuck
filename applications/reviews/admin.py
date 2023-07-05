from django.contrib import admin
from .models import Rating, Comment, Favorite


admin.site.register([Rating, Comment, Favorite])
