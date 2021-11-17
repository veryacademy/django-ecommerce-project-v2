from django.core import serializers
from django.shortcuts import render
from ecommerce.inventory import models


def home(request):

    return render(request, "index.html")


def category(request):

    data = models.Category.objects.all()

    return render(request, "categories.html", {"data": data})


def category(request):

    data = models.Category.objects.all()

    return render(request, "categories.html", {"data": data})


def product_by_category(request, category):

    x = models.Product.objects.filter(category__name="fashion")
    print(models.Product.objects.filter(category__name="fashion").explain(verbose=True, analyze=True))

    y = models.Product.objects.filter(category__name=category).values(
        "id", "name", "created_at", "category__name", "product__store_price"
    )

    # data = serializers.serialize("json", x, indent=4)

    return render(request, "product_by_category.html", {"data": y})


def product_detail(request, slug):

    # x = models.Product.objects.filter(slug=slug)

    x = models.ProductInventory.objects.filter(product__slug=slug).values("product__name", "store_price")

    return render(request, "product_detail.html", {"data": x})
