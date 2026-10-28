"""
URL configuration for catalogue_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Products app URLs
    path('products/', include('products.urls')),

    # Redirect root to products
    path('', RedirectView.as_view(url='/products/', permanent=False)),
]

# Serve media and static files in development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

# Customize admin site headers
admin.site.site_header = "Product Catalogue Administration"
admin.site.site_title = "Product Catalogue Admin"
admin.site.index_title = "Welcome to Product Catalogue Admin Panel"