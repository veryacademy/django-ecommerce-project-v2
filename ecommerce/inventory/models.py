from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    """
    Category Table implimented with MPTT.
    """

    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name=_("Category safe URL"), max_length=255, unique=True
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )
    is_active = models.BooleanField(default=True)  # Example Seasonal Lines

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product table
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
    category = TreeManyToManyField(Category)

    def __str__(self):
        return self.name


class ProductInventory(models.Model):
    """
    ProductInventory table
    """

    sku = models.CharField(max_length=255, unique=True)
    product = models.ForeignKey(
        Product, related_name="inventory", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.product.name


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


class ProductType(models.Model):
    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("Required"),
        max_length=255,
    )

    def __str__(self):
        return self.name


class ProductTypeAttributeValues(models.Model):
    producttype = models.ForeignKey(
        ProductType,
        related_name="producttype",
        on_delete=models.CASCADE,
    )
    attributevalues = models.ForeignKey(
        "ProductAttributeValue",
        related_name="attributevaluesss",
        on_delete=models.CASCADE,
    )


class ProductAttributeValue(models.Model):
    """
    table
    """

    productinventory = models.ManyToManyField(
        ProductInventory,
        related_name="productattributevalues",
        through=ProductAttributeValues,
        through_fields=("attributevalues", "productinventory"),
    )
    producttype = models.ManyToManyField(
        ProductType,
        related_name="producttypeattributevalues",
        through=ProductTypeAttributeValues,
        through_fields=("attributevalues", "producttype"),
    )

    attributevalue = models.CharField(
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
    attribute = models.ForeignKey(
        ProductAttribute,
        related_name="attribute",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.attribute.name} - {self.attributevalue}"


class ProductMedia(models.Model):
    """
    The Product Image table.
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_image"
    )
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alturnative text"),
        help_text=_("Please add alturnative text"),
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
