from django.db import models
from django.utils import timezone


class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('No Internet Connection', 'No Internet Connection'),
        ('Slow Internet Speed', 'Slow Internet Speed'),
        ('Router Problem', 'Router Problem'),
        ('Frequent Disconnection', 'Frequent Disconnection'),
        ('Billing Issue', 'Billing Issue'),
        ('Installation Delay', 'Installation Delay'),
        ('Package Upgrade Issue', 'Package Upgrade Issue'),
        ('Technician Visit Delay', 'Technician Visit Delay'),
        ('Customer Support Issue', 'Customer Support Issue'),
        ('Other', 'Other'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Technician Assigned', 'Technician Assigned'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]

    CONTACT_CHOICES = [
        ('Phone', 'Phone'),
        ('Email', 'Email'),
        ('Either', 'Either'),
    ]

    reference_number = models.CharField(max_length=25, unique=True, db_index=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    customer_id = models.CharField(max_length=50, blank=True)
    address_area = models.CharField(max_length=160)
    category = models.CharField(max_length=60, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=160)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium')
    preferred_contact = models.CharField(max_length=20, choices=CONTACT_CHOICES, default='Phone')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')
    admin_note = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.reference_number} - {self.title}'


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=160)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.subject} from {self.name}'
