from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin

from .serializers import CommentSerializer, RatingSerializer, FavoriteSerializer
from .models import Comment, Rating, Favorite
from permissions import IsOwnerOrIsAdminUser


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        elif self.request.method in ['DELETE', 'PATCH', 'PUT']:
            self.permission_classes = [IsOwnerOrIsAdminUser]
        return super().get_permissions()


class RatingViewSet(CreateModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated] 
        else:
            self.permission_classes = [IsOwnerOrIsAdminUser]
        return super().get_permissions()



class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)