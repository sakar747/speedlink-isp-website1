from django import forms
from .models import Complaint, ContactMessage


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = [
            'full_name', 'email', 'phone', 'customer_id', 'address_area',
            'category', 'title', 'description', 'priority', 'preferred_contact'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'e.g. Sakar Shrestha'}),
            'email': forms.EmailInput(attrs={'placeholder': 'e.g. customer@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': 'e.g. 9800000000'}),
            'customer_id': forms.TextInput(attrs={'placeholder': 'e.g. SL-1023, optional'}),
            'address_area': forms.TextInput(attrs={'placeholder': 'e.g. Baneshwor, Kathmandu'}),
            'title': forms.TextInput(attrs={'placeholder': 'Short title of your internet issue'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe the issue clearly...', 'rows': 5}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'How can we help?'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your message...', 'rows': 5}),
        }
