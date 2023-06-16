from rest_framework import serializers
from .models import ProductImage, Product


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ["product"]


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )

    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
            "slug": {"read_only": True},
        }

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["user"] = user
        images = validated_data.pop("image", None)
        product = Product.objects.create(**validated_data)
        if images is not None:
            imgs = []
            for image in images:
                imgs.append(ProductImage(product=product, image=image))
            ProductImage.objects.bulk_create(imgs)
        return product

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["images"] = ProductImageSerializer(
            instance.images.all(), many=True
        ).data
        return representation
