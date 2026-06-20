from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .chatbot import get_chatbot_reply
from .forms import ComplaintForm, ContactForm
from .models import Complaint
from .utils import generate_reference_number, status_class


def home(request):
    stats = {
        'packages': 4,
        'support': '24/7',
        'response': 'Fast',
    }
    return render(request, 'complaints/home.html', {'stats': stats})


def about(request):
    return render(request, 'complaints/about.html')


def services(request):
    services_list = [
        {'title': 'Home Internet', 'text': 'Reliable fibre internet for students, families and daily browsing.', 'icon': '🏠'},
        {'title': 'Business Internet', 'text': 'Stable internet support for small offices and local businesses.', 'icon': '🏢'},
        {'title': 'Router Support', 'text': 'Help for router setup, red light issues and Wi-Fi performance.', 'icon': '📶'},
        {'title': 'Installation Support', 'text': 'Guidance for new connection setup and technician visits.', 'icon': '🛠️'},
        {'title': 'Package Upgrade', 'text': 'Support for customers who need more speed or package changes.', 'icon': '⚡'},
        {'title': 'Complaint Support', 'text': 'Online complaint submission, tracking and staff follow-up.', 'icon': '🎧'},
    ]
    return render(request, 'complaints/services.html', {'services_list': services_list})


def packages(request):
    plans = [
        {'name': 'Basic Home', 'speed': '25 Mbps', 'price': 'Rs. 999', 'tag': 'Students', 'features': ['Smooth browsing', 'Online classes', 'Basic support']},
        {'name': 'Family Plus', 'speed': '50 Mbps', 'price': 'Rs. 1,499', 'tag': 'Popular', 'features': ['Streaming', 'Multiple devices', 'Router support']},
        {'name': 'Premium Fibre', 'speed': '100 Mbps', 'price': 'Rs. 2,299', 'tag': 'Fast', 'features': ['Gaming', 'Work from home', 'Priority support']},
        {'name': 'Business Pro', 'speed': '150 Mbps', 'price': 'Rs. 3,999', 'tag': 'Business', 'features': ['Office use', 'High uptime', 'Dedicated support']},
    ]
    return render(request, 'complaints/packages.html', {'plans': plans})


def support(request):
    troubleshooting = [
        {
            'title': 'No Internet Connection',
            'steps': ['Check router power light.', 'Check fibre/LAN cable.', 'Restart router for 2–3 minutes.', 'Check bill status.'],
        },
        {
            'title': 'Slow Internet Speed',
            'steps': ['Restart router.', 'Move closer to Wi-Fi.', 'Disconnect extra devices.', 'Stop downloads and test again.'],
        },
        {
            'title': 'Router Red Light',
            'steps': ['Check cable connection.', 'Restart router.', 'Check WAN/Internet light.', 'Submit complaint if red light stays.'],
        },
        {
            'title': 'Payment Not Updated',
            'steps': ['Check transaction ID.', 'Confirm customer ID.', 'Wait normal update time.', 'Submit billing issue if not updated.'],
        },
    ]
    return render(request, 'complaints/support.html', {'troubleshooting': troubleshooting})


def assistant(request):
    return render(request, 'complaints/assistant.html')


@require_POST
def assistant_reply(request):
    message = request.POST.get('message', '')
    data = get_chatbot_reply(message)
    return JsonResponse(data)


def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.reference_number = generate_reference_number()
            complaint.status = 'Pending'
            complaint.save()
            return redirect('complaint_success', reference_number=complaint.reference_number)
    else:
        initial_category = request.GET.get('category')
        initial_priority = request.GET.get('priority')
        form = ComplaintForm(initial={
            'category': initial_category if initial_category in dict(Complaint.CATEGORY_CHOICES) else None,
            'priority': initial_priority if initial_priority in dict(Complaint.PRIORITY_CHOICES) else None,
        })
    return render(request, 'complaints/submit_complaint.html', {'form': form})


def complaint_success(request, reference_number):
    complaint = get_object_or_404(Complaint, reference_number=reference_number)
    return render(request, 'complaints/complaint_success.html', {'complaint': complaint})


def track_complaint(request):
    complaint = None
    searched = False
    reference = ''
    if request.method == 'POST':
        searched = True
        reference = request.POST.get('reference_number', '').strip().upper()
        if reference:
            complaint = Complaint.objects.filter(reference_number__iexact=reference).first()
    return render(request, 'complaints/track_complaint.html', {
        'complaint': complaint,
        'searched': searched,
        'reference': reference,
        'status_class': status_class(complaint.status) if complaint else '',
    })


def faq(request):
    faqs = [
        ('How do I submit a complaint?', 'Open Submit Complaint, fill in your details and save the reference number shown after submission.'),
        ('How do I track my complaint?', 'Use the Track Complaint page and enter your reference number exactly as provided.'),
        ('What should I do if internet is slow?', 'Restart your router, test near the router, disconnect extra devices and submit a complaint if speed remains poor.'),
        ('What if my payment is not updated?', 'Check your customer ID, receipt and transaction ID, then submit a Billing Issue complaint if it remains unresolved.'),
        ('What does Technician Assigned mean?', 'It means ISP staff have assigned the issue to a technician for checking or repair.'),
        ('Is the chatbot a full AI model?', 'This prototype uses rule-based smart support to suggest troubleshooting steps, category and priority.'),
    ]
    return render(request, 'complaints/faq.html', {'faqs': faqs})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you. Your message has been recorded successfully.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'complaints/contact.html', {'form': form})


def staff_login(request):
    if request.session.get('staff_logged_in'):
        return redirect('admin_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == settings.STAFF_USERNAME and password == settings.STAFF_PASSWORD:
            request.session['staff_logged_in'] = True
            messages.success(request, 'Welcome to the SpeedLink admin dashboard.')
            return redirect('admin_dashboard')
        messages.error(request, 'Invalid username or password.')

    return render(request, 'complaints/admin_login.html')


def staff_logout(request):
    request.session.pop('staff_logged_in', None)
    messages.success(request, 'You have been logged out.')
    return redirect('staff_login')


def staff_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('staff_logged_in'):
            messages.error(request, 'Please log in to access the admin area.')
            return redirect('staff_login')
        return view_func(request, *args, **kwargs)
    return wrapper


@staff_required
def admin_dashboard(request):
    complaints = Complaint.objects.all()

    status = request.GET.get('status', '')
    category = request.GET.get('category', '')
    priority = request.GET.get('priority', '')
    search = request.GET.get('search', '').strip()

    if status:
        complaints = complaints.filter(status=status)
    if category:
        complaints = complaints.filter(category=category)
    if priority:
        complaints = complaints.filter(priority=priority)
    if search:
        complaints = complaints.filter(
            Q(reference_number__icontains=search) |
            Q(full_name__icontains=search) |
            Q(phone__icontains=search) |
            Q(title__icontains=search)
        )

    counts = {
        'total': Complaint.objects.count(),
        'pending': Complaint.objects.filter(status='Pending').count(),
        'progress': Complaint.objects.filter(status='In Progress').count(),
        'tech': Complaint.objects.filter(status='Technician Assigned').count(),
        'resolved': Complaint.objects.filter(status='Resolved').count(),
        'closed': Complaint.objects.filter(status='Closed').count(),
    }

    return render(request, 'complaints/admin_dashboard.html', {
        'complaints': complaints,
        'counts': counts,
        'categories': Complaint.CATEGORY_CHOICES,
        'priorities': Complaint.PRIORITY_CHOICES,
        'statuses': Complaint.STATUS_CHOICES,
        'filters': {'status': status, 'category': category, 'priority': priority, 'search': search},
    })


@staff_required
def complaint_detail(request, reference_number):
    complaint = get_object_or_404(Complaint, reference_number=reference_number)
    return render(request, 'complaints/complaint_detail.html', {'complaint': complaint})


@staff_required
@require_POST
def update_complaint(request, reference_number):
    complaint = get_object_or_404(Complaint, reference_number=reference_number)
    new_status = request.POST.get('status')
    admin_note = request.POST.get('admin_note', '')
    if new_status in dict(Complaint.STATUS_CHOICES):
        complaint.status = new_status
        complaint.admin_note = admin_note
        complaint.save()
        messages.success(request, f'{complaint.reference_number} updated successfully.')
    else:
        messages.error(request, 'Invalid status selected.')
    return redirect('complaint_detail', reference_number=complaint.reference_number)
