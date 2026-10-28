"""
URL configuration for products app
"""
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Product list page (homepage)
    path(
        '',
        views.product_list_view,
        name='product_list'
    ),

    # Product detail page
    path(
        '<slug:slug>/',
        views.product_detail_view,
        name='product_detail'
    ),

    # Alternative URLs using class-based views
    # Uncomment these and comment out the function-based views above to use CBVs
    # path(
    #     '',
    #     views.ProductListView.as_view(),
    #     name='product_list'
    # ),
    # path(
    #     'product/<slug:slug>/',
    #     views.ProductDetailView.as_view(),
    #     name='product_detail'
    # ),
]