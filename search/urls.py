from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from search.views import ProductViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
