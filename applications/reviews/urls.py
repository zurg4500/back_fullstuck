from rest_framework import routers

from .views import CommentViewSet, FavoriteViewSet, RatingViewSet


router = routers.DefaultRouter()
router.register('comment', CommentViewSet, 'comment')
router.register('favorite', FavoriteViewSet, 'favorite')
router.register('ratings', RatingViewSet, 'ratings')


urlpatterns = router.urls
