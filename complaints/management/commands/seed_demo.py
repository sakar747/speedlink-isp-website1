from django.core.management.base import BaseCommand
from complaints.models import Complaint
from complaints.utils import generate_reference_number


class Command(BaseCommand):
    help = 'Create sample SpeedLink ISP complaints for demonstration.'

    def handle(self, *args, **options):
        samples = [
            {
                'full_name': 'Sakar Shrestha',
                'email': 'sakar@example.com',
                'phone': '9800000001',
                'customer_id': 'SL-1001',
                'address_area': 'Baneshwor, Kathmandu',
                'category': 'No Internet Connection',
                'title': 'Internet not working since morning',
                'description': 'Router power is on but the internet light is red.',
                'priority': 'High',
                'preferred_contact': 'Phone',
                'status': 'Technician Assigned',
                'admin_note': 'Technician assigned for line check today.',
            },
            {
                'full_name': 'Nisha Karki',
                'email': 'nisha@example.com',
                'phone': '9800000002',
                'customer_id': 'SL-1002',
                'address_area': 'Patan, Lalitpur',
                'category': 'Slow Internet Speed',
                'title': 'Wi-Fi very slow during evening',
                'description': 'Speed drops in the evening on all devices.',
                'priority': 'Medium',
                'preferred_contact': 'Email',
                'status': 'In Progress',
                'admin_note': 'Support team checking area load.',
            },
            {
                'full_name': 'Aman Lama',
                'email': 'aman@example.com',
                'phone': '9800000003',
                'customer_id': 'SL-1003',
                'address_area': 'Koteshwor, Kathmandu',
                'category': 'Billing Issue',
                'title': 'Payment completed but account blocked',
                'description': 'I paid yesterday but my internet is still blocked.',
                'priority': 'Medium',
                'preferred_contact': 'Phone',
                'status': 'Pending',
                'admin_note': '',
            },
        ]
        created = 0
        for sample in samples:
            if not Complaint.objects.filter(customer_id=sample['customer_id'], title=sample['title']).exists():
                Complaint.objects.create(reference_number=generate_reference_number(), **sample)
                created += 1
        self.stdout.write(self.style.SUCCESS(f'Created {created} demo complaint(s).'))
