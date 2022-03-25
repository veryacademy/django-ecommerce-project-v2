from django.contrib import admin

from . import models

admin.site.register(models.Product)
admin.site.register(models.Category)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ("product", "store_price")


admin.site.register(models.ProductInventory, InventoryAdmin)
