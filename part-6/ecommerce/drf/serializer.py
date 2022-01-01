from django.db.models.fields.related import ManyToManyField
from ecommerce.inventory.models import (
    Brand,
    Category,
    Media,
    Product,
    ProductAttributeValue,
    ProductInventory,
    ProductType,
)
from rest_framework import serializers


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        # fields = "__all__"
        depth = 2
        exclude = ["id"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ["name"]


class MediaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["img_url", "alt_text"]
        read_only = True
        editable = False

    def get_img_url(self, obj):
        return self.context["request"].build_absolute_uri(obj.img_url.url)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["name"]
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):

    product= ProductSerializer(many=False, read_only=True)

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "product",
        ]
        read_only = True


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ["web_id", "slug", "name", "description", "category", "product"]


# class AllProductSerializer(serializers.HyperlinkedModelSerializer):
#     category = serializers.StringRelatedField(many=True)
#     product = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Product
#         fields = ["web_id", "slug", "name", "description", "category", "product"]
#         read_only = True
#         editable = False


# class SingleProductSerializer(serializers.HyperlinkedModelSerializer):
#     # category = serializers.StringRelatedField(many=True)
#     # # product = serializers.StringRelatedField(many=True)
#     # product = ProductInventorySerializer(many=True, read_only=True)
#     # Nested Approach
#     web_id = ProductSerializer(many=True, read_only=True)

#     class Meta:
#         model = ProductInventory
#         fields = ["sku", "retail_price", "is_default", "web_id"]
