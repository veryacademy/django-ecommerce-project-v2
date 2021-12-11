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

    # x = models.Product.objects.filter(category__name="fashion")
    # print(models.Product.objects.filter(category__name="fashion").explain(verbose=True, analyze=True))

    y = models.Product.objects.filter(category__name=category).filter(product__is_default=True).values(
        "id", "name", "slug", "created_at", "category__name", "product__store_price"
    )

    # data = serializers.serialize("json", x, indent=4)

    return render(request, "product_by_category.html", {"data": y})


def product_detail(request, slug):

    # x = models.Product.objects.filter(slug=slug)

    # x = models.ProductInventory.objects.filter(product__slug=slug).values("id", "product__name", "store_price", "is_default", "attribute_values__attribute_value")

    # Using chained filters approach
    # x = models.ProductInventory.objects.filter(product__slug=slug).filter(attribute_values__attribute_value="red").filter(attribute_values__attribute_value=5).select_related('product')

    # from django.db.models import Count
    # filter_arguments = [5, "red"]
    # x = models.ProductInventory.objects.filter(product__slug=slug).filter(attribute_values__attribute_value__in=filter_arguments).annotate(num_tags=Count('attribute_values')).filter(num_tags=len(filter_arguments))


    # Dynamic Filter
    filter_arguments = []

    if request.GET:
        for value in request.GET.values():
            filter_arguments.append(value)

        from django.db.models import Count
        from django.contrib.postgres.aggregates import ArrayAgg

        x = models.ProductInventory.objects.filter(product__slug=slug).filter(attribute_values__attribute_value__in=filter_arguments).annotate(num_tags=Count('attribute_values')).filter(num_tags=len(filter_arguments)).values(
        "id", "sku", "product__name", "store_price", "product_inventory__units").annotate(field_a=ArrayAgg("attribute_values__attribute_value")).get()
    else:

        from django.contrib.postgres.aggregates import ArrayAgg

        x = models.ProductInventory.objects.filter(product__slug=slug).filter(is_default=True).values(
        "id", "sku", "product__name", "store_price", "product_inventory__units").annotate(field_a=ArrayAgg("attribute_values__attribute_value")).get()

        
    y = models.ProductInventory.objects.filter(product__slug=slug).distinct().values(
    "attribute_values__product_attribute__name", "attribute_values__attribute_value")

    z = models.ProductTypeAttribute.objects.filter(product_type__product_type__product__slug=slug).distinct().values("product_attribute__name")

    return render(request, "product_detail.html", {"x": x, "filter": y, "z" : z})

