from django import forms
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from ecommerce.inventory.models import (
    Category,
    Product,
    ProductAttribute,
    ProductAttributeValue,
    ProductInventory,
    ProductType,
    ProductTypeAttributeValues,
    Stock,
)
from mptt.admin import MPTTModelAdmin
from mptt.models import TreeManyToManyField


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue.product_inventory.through


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductAttributeValueInline,
    ]


class ProductTypeAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue.product_type.through


@admin.register(ProductType)
class ProductInventoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductTypeAttributeValueInline,
    ]


class filterCategories(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(filterCategories, self).__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.filter(
            children=None
        )


class ProductAdmin(admin.ModelAdmin):
    form = filterCategories
    formfield_overrides = {
        TreeManyToManyField: {"widget": CheckboxSelectMultiple},
    }


class CustomMPTTModelAdmin(MPTTModelAdmin):

    prepopulated_fields = {
        "slug": ("name",),
    }


# admin.site.register(ProductTypeAttributeValue)
# admin.site.register(ProductType)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CustomMPTTModelAdmin)
admin.site.register(Stock)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
