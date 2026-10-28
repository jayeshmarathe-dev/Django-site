from django.core.management.base import BaseCommand
from django.utils.text import slugify
from products.models import Category, Product
from decimal import Decimal


class Command(BaseCommand):
    help = 'Populates the database with sample products and categories'

    def handle(self, *args, **options):
        self.stdout.write('Starting database population...\n')

        # Clear existing data
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.WARNING('Cleared existing data\n'))

        # Create categories
        categories_data = [
            {
                'name': 'Electronics',
                'description': 'Latest electronic gadgets and devices'
            },
            {
                'name': 'Computing',
                'description': 'Computers, laptops, and accessories'
            },
            {
                'name': 'Audio',
                'description': 'Speakers, headphones, and audio equipment'
            },
            {
                'name': 'Gaming',
                'description': 'Gaming consoles and accessories'
            },
            {
                'name': 'Accessories',
                'description': 'Tech accessories and peripherals'
            },
        ]

        categories = {}
        for cat_data in categories_data:
            category = Category.objects.create(**cat_data)
            categories[cat_data['name']] = category
            self.stdout.write(
                self.style.SUCCESS(f'✓ Created category: {category.name}')
            )

        # Create products
        products_data = [
            {
                'name': 'Wireless Bluetooth Headphones Pro',
                'category': 'Audio',
                'description': 'Premium wireless headphones with active noise cancellation, 40-hour battery life, and superior sound quality. Features comfortable over-ear design with memory foam cushions. Perfect for music lovers, travelers, and professionals who demand the best audio experience.',
                'price': Decimal('7999.00'),
                'discount_price': Decimal('5999.00'),
                'stock': 45,
                'featured': True,
            },
            {
                'name': 'Smart Watch Ultra Series 5',
                'category': 'Electronics',
                'description': 'Advanced fitness tracking smartwatch with heart rate monitoring, GPS, blood oxygen sensor, and 7-day battery life. Water-resistant up to 50m with customizable watch faces. Includes sleep tracking, stress monitoring, and smartphone notifications.',
                'price': Decimal('29999.00'),
                'discount_price': Decimal('24999.00'),
                'stock': 30,
                'featured': True,
            },
            {
                'name': 'Ultra Portable Power Bank 30000mAh',
                'category': 'Accessories',
                'description': 'High-capacity power bank with 30000mAh battery, fast charging support, and 3 USB ports. Charge multiple devices simultaneously with intelligent power distribution. LED display shows remaining battery percentage. Compact design with aluminum body.',
                'price': Decimal('2999.00'),
                'discount_price': Decimal('1999.00'),
                'stock': 100,
                'featured': False,
            },
            {
                'name': 'HD Pro Webcam 1080p',
                'category': 'Computing',
                'description': 'Professional webcam with 1080p Full HD resolution, auto-focus, and built-in dual microphones. Features wide-angle lens for group calls, low-light correction, and plug-and-play USB connectivity. Perfect for video conferencing, streaming, and content creation.',
                'price': Decimal('4999.00'),
                'discount_price': Decimal('3499.00'),
                'stock': 55,
                'featured': False,
            },
            {
                'name': 'Mechanical Gaming Keyboard RGB',
                'category': 'Gaming',
                'description': 'Premium mechanical keyboard with customizable RGB backlighting, Cherry MX switches, and anti-ghosting technology. Features dedicated media controls, aluminum frame, and detachable USB-C cable. Includes wrist rest for extended gaming sessions.',
                'price': Decimal('8999.00'),
                'discount_price': Decimal('6999.00'),
                'stock': 35,
                'featured': True,
            },
            {
                'name': 'Wireless Gaming Mouse Pro',
                'category': 'Gaming',
                'description': 'High-precision wireless gaming mouse with 16000 DPI sensor, programmable buttons, and ergonomic design. Features RGB lighting, 70-hour battery life, and 1ms response time. Comes with interchangeable side grips and weights.',
                'price': Decimal('3999.00'),
                'discount_price': Decimal('2999.00'),
                'stock': 60,
                'featured': False,
            },
            {
                'name': 'USB-C Hub Multiport Adapter',
                'category': 'Accessories',
                'description': '10-in-1 USB-C hub with HDMI 4K output, 3 USB 3.0 ports, SD/TF card readers, Ethernet port, and USB-C power delivery. Aluminum construction with heat dissipation design. Compatible with MacBook, laptops, and tablets.',
                'price': Decimal('2499.00'),
                'discount_price': None,
                'stock': 80,
                'featured': False,
            },
            {
                'name': 'Adjustable Aluminum Laptop Stand',
                'category': 'Accessories',
                'description': 'Ergonomic laptop stand with 6-level height adjustment, 360-degree rotation, and ventilation design. Made from premium aluminum alloy with anti-slip silicone pads. Supports laptops from 10 to 17 inches. Foldable and portable design.',
                'price': Decimal('1499.00'),
                'discount_price': None,
                'stock': 120,
                'featured': False,
            },
            {
                'name': 'RGB Laptop Cooling Pad 6-Fan',
                'category': 'Computing',
                'description': 'Advanced cooling pad with 6 ultra-quiet fans, RGB lighting, and adjustable fan speeds. Features ergonomic design with 7 height settings, dual USB ports, and anti-slip surface. Supports laptops up to 17.3 inches.',
                'price': Decimal('2999.00'),
                'discount_price': Decimal('1999.00'),
                'stock': 70,
                'featured': False,
            },
            {
                'name': 'External SSD 2TB Portable',
                'category': 'Computing',
                'description': 'Ultra-fast portable SSD with read speeds up to 1050MB/s and write speeds up to 1000MB/s. USB 3.2 Gen 2 interface with USB-C and USB-A cables included. Compact aluminum design with hardware encryption. Compatible with PC, Mac, and gaming consoles.',
                'price': Decimal('14999.00'),
                'discount_price': Decimal('11999.00'),
                'stock': 40,
                'featured': True,
            },
            {
                'name': 'LED Desk Lamp with Wireless Charger',
                'category': 'Accessories',
                'description': 'Smart desk lamp with adjustable brightness, color temperature control, and built-in wireless charging pad. Features touch controls, USB charging port, and timer function. Eye-caring LED with flicker-free technology.',
                'price': Decimal('2499.00'),
                'discount_price': Decimal('1799.00'),
                'stock': 90,
                'featured': False,
            },
            {
                'name': 'Waterproof Bluetooth Speaker 360°',
                'category': 'Audio',
                'description': 'Rugged waterproof Bluetooth speaker with 360-degree sound, 20-hour battery life, and deep bass. IPX7 waterproof rating for pool and beach use. Features built-in power bank, hands-free calls, and multi-connect for stereo pairing.',
                'price': Decimal('3999.00'),
                'discount_price': Decimal('2999.00'),
                'stock': 65,
                'featured': False,
            },
            {
                'name': 'Wireless Earbuds Pro with ANC',
                'category': 'Audio',
                'description': 'Premium true wireless earbuds with active noise cancellation, transparency mode, and 8-hour playback. Charging case provides 32 hours total. Features touch controls, IPX5 water resistance, and premium sound quality with deep bass.',
                'price': Decimal('4999.00'),
                'discount_price': Decimal('3999.00'),
                'stock': 50,
                'featured': False,
            },
            {
                'name': 'Gaming Headset 7.1 Surround Sound',
                'category': 'Gaming',
                'description': 'Professional gaming headset with virtual 7.1 surround sound, noise-cancelling microphone, and RGB lighting. Features 50mm drivers, memory foam cushions, and multi-platform compatibility. Wired connection with USB and 3.5mm options.',
                'price': Decimal('5999.00'),
                'discount_price': Decimal('4499.00'),
                'stock': 45,
                'featured': False,
            },
            {
                'name': '4K Ultra HD Monitor 27-inch',
                'category': 'Computing',
                'description': '27-inch 4K UHD monitor with IPS panel, 99% sRGB color gamut, and HDR support. Features 60Hz refresh rate, 5ms response time, and VESA mount compatibility. Includes HDMI, DisplayPort, and USB-C connectivity with built-in speakers.',
                'price': Decimal('24999.00'),
                'discount_price': Decimal('19999.00'),
                'stock': 25,
                'featured': True,
            },
            {
                'name': 'Graphics Tablet with Pen Display',
                'category': 'Computing',
                'description': 'Professional graphics tablet with 13.3-inch display, 8192 pressure levels, and battery-free pen. Features Full HD resolution, 120% sRGB color gamut, and customizable express keys. Perfect for digital artists, designers, and photographers.',
                'price': Decimal('18999.00'),
                'discount_price': None,
                'stock': 20,
                'featured': False,
            },
            {
                'name': 'Smart Home Security Camera 2K',
                'category': 'Electronics',
                'description': '2K resolution security camera with night vision, motion detection, and two-way audio. Features AI person detection, cloud storage, and mobile app control. Weather-resistant design for indoor and outdoor use.',
                'price': Decimal('3499.00'),
                'discount_price': Decimal('2499.00'),
                'stock': 75,
                'featured': False,
            },
            {
                'name': 'Wireless Charging Pad Triple',
                'category': 'Accessories',
                'description': '3-in-1 wireless charging station for phone, watch, and earbuds. Features fast charging with up to 15W output, LED indicator, and anti-slip design. Compatible with all Qi-enabled devices. Includes wall adapter.',
                'price': Decimal('2999.00'),
                'discount_price': Decimal('1999.00'),
                'stock': 85,
                'featured': False,
            },
        ]

        for product_data in products_data:
            # Get category object
            category_name = product_data.pop('category')
            product_data['category'] = categories[category_name]

            # Generate slug from name
            product_data['slug'] = slugify(product_data['name'])

            # Create product
            product = Product.objects.create(**product_data)

            self.stdout.write(
                self.style.SUCCESS(
                    f'✓ Created product: {product.name} '
                    f'(₹{product.price})'
                )
            )

        # Display summary
        total_products = Product.objects.count()
        total_categories = Category.objects.count()
        featured_count = Product.objects.filter(featured=True).count()

        self.stdout.write('\n' + '=' * 60)
        self.stdout.write(self.style.SUCCESS('\n✓ Database population completed!\n'))
        self.stdout.write(f'Total Categories: {total_categories}')
        self.stdout.write(f'Total Products: {total_products}')
        self.stdout.write(f'Featured Products: {featured_count}')
        self.stdout.write('=' * 60 + '\n')