from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("categories/", views.category),
    path("product-by-category/<slug:category>/", views.product_by_category, name="product_by_category"),
    path("<slug:slug>", views.product_detail, name="product_detail"),
]
