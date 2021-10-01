from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    """
    Category Table implimented with MPTT.
    """

    name = models.CharField(
        verbose_name=_("category name"),
        help_text=_("required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name=_("category safe URL"),
        max_length=255,
        help_text=_("automatically generated from name"),
        unique=True,
    )
    parent = TreeForeignKey(
        "self",
        verbose_name=_("parent category"),
        help_text=_("select <b>parent</b> category"),
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="children",
    )
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product table
    """

    web_id = models.CharField(
        max_length=50,
        verbose_name=_("product website ID"),
        help_text=_("product web ID - must be unique"),
        unique=True,
        # blank=True,
        # null=True,
    )
    slug = models.SlugField(max_length=255)
    name = models.CharField(
        verbose_name=_("product name"),
        help_text=_("required"),
        max_length=255,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("product description"),
        blank=False,
        null=False,
    )
    category = TreeManyToManyField(Category)
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )
    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("Required"),
        max_length=255,
    )

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("Required"),
        max_length=255,
    )
    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False
    )


class ProductInventory(models.Model):
    """
    ProductInventory table
    """

    sku = models.CharField(max_length=255, unique=True)
    upc = models.CharField(max_length=12, unique=True)
    product_type = models.ForeignKey(
        ProductType, related_name="product_type", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="product", on_delete=models.CASCADE
    )
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )
    retail_price = models.DecimalField(
        verbose_name=_("Recommended retail price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    store_price = models.DecimalField(
        verbose_name=_("Regular price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    sale_price = models.DecimalField(
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
    in_stock = models.BooleanField(
        verbose_name=_("Stock Availability"),
        help_text=_("Stock Availability"),
        default=True,
    )
    weight = models.FloatField(_("weight"))
    brand = models.ForeignKey(
        Brand, related_name="brand", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )

    def __str__(self):
        return self.product.name


class Stock(models.Model):
    product_inventory = models.ForeignKey(
        ProductInventory,
        related_name="product_inventory",
        on_delete=models.CASCADE,
    )
    last_checked = models.DateTimeField(_("Stock Check Date"))
    units = models.IntegerField()
    units_sold = models.IntegerField()


class ProductAttribute(models.Model):
    """
    ProductAttribute table
    """

    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("Required"),
        max_length=255,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Product Description"),
        blank=True,
    )

    def __str__(self):
        return self.name


class ProductAttributeValues(models.Model):
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


class ProductTypeAttributeValues(models.Model):
    product_type = models.ForeignKey(
        ProductType,
        related_name="product_type_product_type",
        on_delete=models.CASCADE,
    )
    attribute_value = models.ForeignKey(
        "ProductAttributeValue",
        related_name="product_type_attribute_value",
        on_delete=models.CASCADE,
    )


class ProductAttributeValue(models.Model):
    """
    table
    """

    product_inventory = models.ManyToManyField(
        ProductInventory,
        related_name="product_attribute_values",
        through=ProductAttributeValues,
        through_fields=("attributevalues", "productinventory"),
    )
    product_type = models.ManyToManyField(
        ProductType,
        related_name="product_type_attribute_values",
        through=ProductTypeAttributeValues,
        through_fields=("attribute_value", "product_type"),
    )
    attribute_value = models.CharField(
        verbose_name=_("value"),
        help_text=_("Required"),
        max_length=255,
        null=True,
    )
    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Product Description"),
        blank=True,
    )
    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name="product_attribute",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.attribute.name} - {self.attributevalue}"


class Media(models.Model):
    """
    The product image table.
    """

    product_inventory = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="media_product_inventory",
    )
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alternative text"),
        help_text=_("Please add alternative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
