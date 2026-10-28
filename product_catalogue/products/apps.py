from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    Configuration for products app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    verbose_name = 'Product Catalogue'

    def ready(self):
        """
        Import signals or perform startup tasks here
        """
        pass