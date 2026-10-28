from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q, Count
from django.conf import settings
from .models import Product, Category


def product_list_view(request):  #chenged line
    """
    Function-based view to display list of products with filtering
    """
    # Get all available products
    products = Product.objects.filter(is_available=True)

    # Get search query
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Get category filter
    category_slug = request.GET.get('category', '')
    selected_category = None
    if category_slug:
        try:
            selected_category = Category.objects.get(name=category_slug)
            products = products.filter(category=selected_category)
        except Category.DoesNotExist:
            pass

    # Get all categories with product count
    categories = Category.objects.annotate(
        product_count=Count('products')
    ).filter(product_count__gt=0)

    # Get featured products
    featured_products = Product.objects.filter(
        is_available=True,
        featured=True
    )[:4]

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'featured_products': featured_products,
        'search_query': search_query,
        'total_products': products.count(),
    }

    return render(request, 'products/product_list.html', context)


def product_detail_view(request, slug):
# def product_list_view(request, slug):
    """
    Function-based view to display single product details
    """
    product = get_object_or_404(
        Product,
        slug=slug,
        is_available=True
    )

    # Get related products from same category
    related_products = Product.objects.filter(
        category=product.category,
        is_available=True
    ).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'related_products': related_products,
    }

    return render(request, 'products/product_detail.html', context)


class ProductListView(ListView):
    """
    Class-based view alternative for product listing
    """
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = getattr(settings, 'PRODUCTS_PER_PAGE', 12)

    def get_queryset(self):
        """
        Get filtered queryset based on search and category
        """
        queryset = Product.objects.filter(is_available=True)

        # Search functionality
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        # Category filter
        category_slug = self.request.GET.get('category', '')
        if category_slug:
            queryset = queryset.filter(category__name=category_slug)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Add extra context data
        """
        context = super().get_context_data(**kwargs)

        # Add categories
        context['categories'] = Category.objects.annotate(
            product_count=Count('products')
        ).filter(product_count__gt=0)

        # Add featured products
        context['featured_products'] = Product.objects.filter(
            is_available=True,
            featured=True
        )[:4]

        # Add search query
        context['search_query'] = self.request.GET.get('search', '')

        # Add total products count
        context['total_products'] = self.get_queryset().count()

        # Add selected category
        category_slug = self.request.GET.get('category', '')
        if category_slug:
            try:
                context['selected_category'] = Category.objects.get(
                    name=category_slug
                )
            except Category.DoesNotExist:
                pass

        return context


class ProductDetailView(DetailView):
    """
    Class-based view alternative for product detail
    """
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        """Only show available products"""
        return Product.objects.filter(is_available=True)

    def get_context_data(self, **kwargs):
        """Add related products to context"""
        context = super().get_context_data(**kwargs)

        # Get related products
        context['related_products'] = Product.objects.filter(
            category=self.object.category,
            is_available=True
        ).exclude(id=self.object.id)[:4]

        return context