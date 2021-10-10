from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    """
    Inventory Category table implimented with MPTT.
    """

    name = models.CharField(
        max_length=255,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category name"),
        help_text=_("format: required, max-255"),
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category safe URL"),
        help_text=_(
            "format: required, letters, numbers, underscores or hyphens"
        ),
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("parent of category"),
        help_text=_("format: not required"),
    )
    is_active = models.BooleanField(
        default=True,
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("product category")
        verbose_name_plural = _("product categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product details table
    """

    web_id = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("product website ID"),
        help_text=_("format: required, unique"),
    )
    slug = models.SlugField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product safe URL"),
        help_text=_(
            "format: required, letters, numbers, underscores or hyphens"
        ),
    )
    name = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product name"),
        help_text=_("format: required, max-255"),
    )
    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product description"),
        help_text=_("format: required"),
    )
    category = TreeManyToManyField(Category)
    is_active = models.BooleanField(
        unique=False,
        null=False,
        blank=False,
        default=True,
        verbose_name=_("product visibility"),
        help_text=_("format: true = show product"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("date product created"),
        help_text=_("format: Y-m-d H:M:S"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date product last updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

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


class ProductAttribute(models.Model):
    """
    ProductAttribute table
    """

    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("attribute name"),
        help_text=_("required"),
        max_length=255,
    )
    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("attribute description"),
        help_text=_("required"),
    )

    def __str__(self):
        return self.name


class ProductAttributeValue(models.Model):
    """
    Product attribute table
    """

    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name="product_attribute",
        on_delete=models.CASCADE,
    )
    attribute_value = models.CharField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("attribute value"),
        help_text=_("Required"),
        max_length=255,
    )

    def __str__(self):
        return f"{self.product_attribute.name} : {self.attribute_value}"


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
    attribute_values = models.ManyToManyField(
        ProductAttributeValue,
        related_name="product_attribute_values",
        through="ProductAttributeValues",
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


class Stock(models.Model):
    product_inventory = models.OneToOneField(
        ProductInventory,
        related_name="product_inventory",
        on_delete=models.PROTECT,
    )
    last_checked = models.DateTimeField(
        _("last stock check date"),
        unique=False,
        null=True,
        blank=True,
    )
    units = models.IntegerField(
        unique=False,
        null=False,
        blank=False,
        default=0,
    )
    units_sold = models.IntegerField(
        unique=False,
        null=False,
        blank=False,
        default=0,
    )


class Media(models.Model):
    """
    The product image table.
    """

    product_inventory = models.ForeignKey(
        ProductInventory,
        on_delete=models.PROTECT,
        related_name="media_product_inventory",
    )
    image = models.ImageField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("alternative text"),
        help_text=_("please add alternative text"),
        max_length=255,
    )
    is_feature = models.BooleanField(
        default=False,
        help_text=_("default image"),
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("product image")
        verbose_name_plural = _("product images")


class ProductAttributeValues(models.Model):
    """
    Product attribute values link table
    """

    attributevalues = models.ForeignKey(
        "ProductAttributeValue",
        related_name="attributevaluess",
        on_delete=models.CASCADE,
    )
    productinventory = models.ForeignKey(
        ProductInventory,
        related_name="productattributevaluess",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = (("attributevalues", "productinventory"),)
