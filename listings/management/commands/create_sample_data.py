from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Create sample data for the application'

    def handle(self, *args, **options):
        # Create sample users if they don't exist
        if not User.objects.filter(username='demo_host').exists():
            demo_host = User.objects.create_user(
                username='demo_host',
                email='host@example.com',
                password='demo123',
                first_name='Demo',
                last_name='Host'
            )
            self.stdout.write(
                self.style.SUCCESS('Created demo host user')
            )
        else:
            demo_host = User.objects.get(username='demo_host')

        # Sample listing data
        sample_listings = [
            {
                'title': 'Cozy Downtown Apartment',
                'description': 'Beautiful apartment in the heart of the city with modern amenities.',
                'price_per_night': Decimal('120.00'),
                'location': 'New York, NY'
            },
            {
                'title': 'Beachfront Villa',
                'description': 'Stunning ocean views and direct beach access for the perfect getaway.',
                'price_per_night': Decimal('350.00'),
                'location': 'Miami, FL'
            },
            {
                'title': 'Mountain Cabin Retreat',
                'description': 'Peaceful cabin surrounded by nature, perfect for hiking enthusiasts.',
                'price_per_night': Decimal('180.00'),
                'location': 'Aspen, CO'
            },
            {
                'title': 'Historic Brownstone',
                'description': 'Charming historic building with vintage character and modern comfort.',
                'price_per_night': Decimal('200.00'),
                'location': 'Boston, MA'
            },
        ]

        # Create sample listings
        for listing_data in sample_listings:
            if not Listing.objects.filter(title=listing_data['title']).exists():
                Listing.objects.create(
                    host=demo_host,
                    **listing_data
                )
                self.stdout.write(
                    self.style.SUCCESS(f'Created listing: {listing_data["title"]}')
                )

        self.stdout.write(
            self.style.SUCCESS('Sample data creation completed!')
        )
