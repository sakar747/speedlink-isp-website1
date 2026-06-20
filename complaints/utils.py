import random
import string
from django.utils import timezone
from .models import Complaint


def generate_reference_number() -> str:
    """Generate a readable unique ISP complaint reference number."""
    year = timezone.now().year
    while True:
        suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        reference = f'ISP-{year}-{suffix}'
        if not Complaint.objects.filter(reference_number=reference).exists():
            return reference


def status_class(status: str) -> str:
    return {
        'Pending': 'status-pending',
        'In Progress': 'status-progress',
        'Technician Assigned': 'status-tech',
        'Resolved': 'status-resolved',
        'Closed': 'status-closed',
    }.get(status, 'status-pending')
