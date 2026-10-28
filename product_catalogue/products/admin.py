from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for Category model
    """
    list_display = [
        'name',
        'get_product_count',
        'created_at'
    ]
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']

    fieldsets = (
        ('Category Information', {
            'fields': ('name', 'description')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def get_product_count(self, obj):
        """Display product count for each category"""
        count = obj.get_product_count()
        return format_html(
            '<span style="color: #417690; font-weight: bold;">{}</span>',
            count
        )

    get_product_count.short_description = 'Products'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface for Product model with advanced features
    """
    list_display = [
        'name',
        'category',
        'display_price',
        'display_stock',
        'is_available',
        'featured',
        'created_at'
    ]

    list_filter = [
        'is_available',
        'featured',
        'category',
        'created_at',
        'updated_at'
    ]

    search_fields = [
        'name',
        'description',
        'slug'
    ]

    list_editable = [
        'is_available',
        'featured'
    ]

    readonly_fields = [
        'created_at',
        'updated_at',
        'display_image'
    ]

    prepopulated_fields = {
        'slug': ('name',)
    }

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'name',
                'slug',
                'category',
                'description'
            )
        }),
        ('Pricing', {
            'fields': (
                'price',
                'discount_price'
            ),
            'description': 'Set product pricing. Discount price is optional.'
        }),
        ('Inventory', {
            'fields': (
                'stock',
                'is_available'
            )
        }),
        ('Media', {
            'fields': (
                'image',
                'display_image'
            )
        }),
        ('Display Options', {
            'fields': ('featured',),
            'description': 'Control how product is displayed on the site.'
        }),
        ('Timestamps', {
            'fields': (
                'created_at',
                'updated_at'
            ),
            'classes': ('collapse',)
        }),
    )

    actions = [
        'make_available',
        'make_unavailable',
        'mark_as_featured',
        'unmark_as_featured'
    ]

    def display_price(self, obj):
        """Display price with discount if applicable"""
        if obj.discount_price:
            return format_html(
                '<span style="text-decoration: line-through; color: #999;">{}</span><br>'
                '<span style="color: #28a745; font-weight: bold;">{}</span> '
                '<span style="color: #dc3545;">(-{}%)</span>',
                obj.get_price_display(),
                obj.get_discount_price_display(),
                obj.get_savings_percentage()
            )
        return format_html(
            '<span style="color: #417690; font-weight: bold;">{}</span>',
            obj.get_price_display()
        )

    display_price.short_description = 'Price'

    def display_stock(self, obj):
        """Display stock status with color coding"""
        if obj.stock == 0:
            color = '#dc3545'  # Red
        elif obj.stock < 5:
            color = '#ffc107'  # Yellow
        else:
            color = '#28a745'  # Green

        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.get_stock_status()
        )

    display_stock.short_description = 'Stock Status'

    def display_image(self, obj):
        """Display product image thumbnail in admin"""
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 200px; '
                'border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);" />',
                obj.image.url
            )
        return format_html(
            '<span style="color: #999;">No image uploaded</span>'
        )

    display_image.short_description = 'Image Preview'

    # Custom actions
    def make_available(self, request, queryset):
        """Bulk action to make products available"""
        updated = queryset.update(is_available=True)
        self.message_user(
            request,
            f'{updated} product(s) marked as available.'
        )

    make_available.short_description = 'Mark selected products as available'

    def make_unavailable(self, request, queryset):
        """Bulk action to make products unavailable"""
        updated = queryset.update(is_available=False)
        self.message_user(
            request,
            f'{updated} product(s) marked as unavailable.'
        )

    make_unavailable.short_description = 'Mark selected products as unavailable'

    def mark_as_featured(self, request, queryset):
        """Bulk action to mark products as featured"""
        updated = queryset.update(featured=True)
        self.message_user(
            request,
            f'{updated} product(s) marked as featured.'
        )

    mark_as_featured.short_description = 'Mark as featured'

    def unmark_as_featured(self, request, queryset):
        """Bulk action to unmark products as featured"""
        updated = queryset.update(featured=False)
        self.message_user(
            request,
            f'{updated} product(s) unmarked as featured.'
        )

    unmark_as_featured.short_description = 'Remove featured status'