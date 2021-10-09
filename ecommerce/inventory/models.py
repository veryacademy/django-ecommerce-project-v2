from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    """
    Category Table implimented with MPTT.
    """

    name = models.CharField(
        max_length=255,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category name"),
        help_text=_("required and unique"),
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category safe URL"),
        help_text=_("letters, numbers, underscores or hyphens"),
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("parent category"),
        help_text=_("select <b>parent</b> category"),
    )
    is_active = models.BooleanField(
        default=True,
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("product category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product table
    """

    web_id = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("product website ID"),
        help_text=_("must be unique"),
    )
    slug = models.SlugField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
    )
    name = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product name"),
        help_text=_("required"),
    )
    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product description"),
        help_text=_("product description"),
    )
    category = TreeManyToManyField(Category)
    is_active = models.BooleanField(
        verbose_name=_("product visibility"),
        help_text=_("default is true"),
        default=True,
    )
    created_at = models.DateTimeField(
        _("created at"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """
    Product Type
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("type of product"),
        help_text=_("required"),
    )

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("brand name"),
        help_text=_("Required"),
        max_length=255,
    )


class ProductInventory(models.Model):
    """
    Sub-Products
    """

    sku = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
    )
    upc = models.CharField(
        max_length=12,
        unique=True,
        null=False,
        blank=False,
    )
    product_type = models.ForeignKey(
        ProductType, related_name="product_type", on_delete=models.PROTECT
    )
    product = models.ForeignKey(
        Product, related_name="product", on_delete=models.PROTECT
    )
    brand = models.ForeignKey(
        Brand, related_name="brand", on_delete=models.PROTECT
    )
    is_active = models.BooleanField(
        verbose_name=_("product visibility"),
        help_text=_("change product visibility"),
        default=True,
    )
    retail_price = models.DecimalField(
        unique=False,
        null=False,
        blank=False,
        max_digits=5,
        decimal_places=2,
        verbose_name=_("recommended retail price"),
        help_text=_("maximum price 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
    )
    store_price = models.DecimalField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("regular price"),
        help_text=_("maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    sale_price = models.DecimalField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Discount price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    weight = models.FloatField(
        _("product weight"),
        unique=False,
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.product.name
