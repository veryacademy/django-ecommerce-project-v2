from typing import List

from ecommerce.inventory.models import Category, Product, ProductInventory
from ninja import NinjaAPI

from .schema import CategorySchema, InventorySchema, ProductSchema

api = NinjaAPI()


@api.get("/inventory/category/all/", response=List[CategorySchema])
def category_list(request):
    qs = Category.objects.all()
    return qs


@api.get(
    "/inventory/products/category/{category_slug}/",
    response=List[ProductSchema],
)
def category_list(request, category_slug: str):
    qs = Product.objects.filter(category__slug=category_slug)
    return qs


@api.get("/inventory/{web_id}/", response=List[InventorySchema])
def inventory_list(request, web_id: str):
    qs = ProductInventory.objects.filter(product__web_id=web_id)
    return qs
