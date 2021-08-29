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
)
from mptt.admin import MPTTModelAdmin
from mptt.models import TreeManyToManyField


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue.productinventory.through


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductAttributeValueInline,
    ]


class ProductTypeAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue.producttype.through


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


# admin.site.register(ProductTypeAttributeValue)
# admin.site.register(ProductType)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
