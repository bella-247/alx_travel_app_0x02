from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from datetime import date, timedelta
import random


class Command(BaseCommand):
    """
    Django management command to seed the database with sample data.
    """

    help = "Seed the database with sample listings, bookings, and reviews."

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write("Clearing existing data...")
        Listing.objects.all().delete()
        Review.objects.all().delete()
        Booking.objects.all().delete()

        # Sample data
        listings_data = [
            {
                "title": "Cozy Cottage",
                "description": "A cozy cottage in the countryside.",
                "price": 120.00,
                "location": "Countryside",
            },
            {
                "title": "Modern Apartment",
                "description": "A modern apartment in the city center.",
                "price": 200.00,
                "location": "City Center",
            },
            {
                "title": "Beach House",
                "description": "A beautiful beach house with ocean views.",
                "price": 350.00,
                "location": "Beachfront",
            },
        ]

        # Create listings
        self.stdout.write("Seeding new listings...")
        for data in listings_data:
            listing = Listing.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))

            # Create sample bookings for each listing
            for _ in range(random.randint(1, 3)):
                start_date = date.today() + timedelta(days=random.randint(1, 30))
                end_date = start_date + timedelta(days=random.randint(2, 7))
                Booking.objects.create(
                    listing=listing,
                    guest_name=f"Guest_{random.randint(100, 999)}",
                    start_date=start_date,
                    end_date=end_date,
                )

            # Create sample reviews
            for _ in range(random.randint(1, 4)):
                Review.objects.create(
                    listing=listing,
                    reviewer_name=f"Reviewer_{random.randint(100, 999)}",
                    rating=random.randint(1, 5),
                    comment=f"A great stay at {listing.title}.",
                )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
