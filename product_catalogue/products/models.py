from django.db import models
from django.urls import reverse
from django.conf import settings


class Category(models.Model):
    """
    Category model for organizing products
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Enter product category name"
    )
    description = models.TextField(
        blank=True,
        help_text="Enter category description"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_product_count(self):
        """Return number of products in this category"""
        return self.products.filter(is_available=True).count()


class Product(models.Model):
    """
    Product model with all essential fields
    """
    name = models.CharField(
        max_length=200,
        db_index=True,
        help_text="Enter the product name"
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text="Unique identifier for URL"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        null=True,
        blank=True,
        help_text="Select product category"
    )
    description = models.TextField(
        help_text="Enter detailed product description"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Enter product price"
    )
    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Enter discounted price (optional)"
    )
    image = models.ImageField(
        upload_to='products/%Y/%m/%d/',
        blank=True,
        null=True,
        help_text="Upload product image"
    )
    stock = models.PositiveIntegerField(
        default=0,
        help_text="Available stock quantity"
    )
    is_available = models.BooleanField(
        default=True,
        help_text="Is product available for purchase?"
    )
    featured = models.BooleanField(
        default=False,
        help_text="Display as featured product?"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return URL for product detail page"""
        return reverse('products:product_detail', args=[self.slug])

    def get_price_display(self):
        """Return formatted price with currency"""
        currency = getattr(settings, 'CURRENCY_SYMBOL', '$')
        return f"{currency}{self.price:,.2f}"

    def get_discount_price_display(self):
        """Return formatted discount price"""
        if self.discount_price:
            currency = getattr(settings, 'CURRENCY_SYMBOL', '$')
            return f"{currency}{self.discount_price:,.2f}"
        return None

    def get_savings(self):
        """Calculate savings if discount price exists"""
        if self.discount_price and self.discount_price < self.price:
            return self.price - self.discount_price
        return 0

    def get_savings_percentage(self):
        """Calculate savings percentage"""
        if self.discount_price and self.discount_price < self.price:
            savings = ((self.price - self.discount_price) / self.price) * 100
            return round(savings)
        return 0

    def is_in_stock(self):
        """Check if product is in stock"""
        return self.stock > 0

    def get_stock_status(self):
        """Return stock status message"""
        if self.stock == 0:
            return "Out of Stock"
        elif self.stock < 5:
            return f"Only {self.stock} left!"
        else:
            return "In Stock"