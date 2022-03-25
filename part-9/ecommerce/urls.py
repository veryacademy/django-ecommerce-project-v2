from django.contrib import admin
from django.urls import path

from ecommerce.drf.views import (
    CategoryList,
    ProductByCategory,
    ProductInventoryByWebId,
)
from ecommerce.search.views import SearchProductInventory

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/inventory/category/all/", CategoryList.as_view()),
    path(
        "api/inventory/products/category/<str:query>/",
        ProductByCategory.as_view(),
    ),
    path("api/inventory/<int:query>/", ProductInventoryByWebId.as_view()),
    path("api/search/<str:query>/", SearchProductInventory.as_view()),
]
