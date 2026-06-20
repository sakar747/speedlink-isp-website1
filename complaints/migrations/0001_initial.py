# Generated for SpeedLink academic prototype.
from django.db import migrations, models
import django.utils.timezone
import django_mongodb_backend.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', django_mongodb_backend.fields.ObjectIdAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=160)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', django_mongodb_backend.fields.ObjectIdAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(db_index=True, max_length=25, unique=True)),
                ('full_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=25)),
                ('customer_id', models.CharField(blank=True, max_length=50)),
                ('address_area', models.CharField(max_length=160)),
                ('category', models.CharField(choices=[('No Internet Connection', 'No Internet Connection'), ('Slow Internet Speed', 'Slow Internet Speed'), ('Router Problem', 'Router Problem'), ('Frequent Disconnection', 'Frequent Disconnection'), ('Billing Issue', 'Billing Issue'), ('Installation Delay', 'Installation Delay'), ('Package Upgrade Issue', 'Package Upgrade Issue'), ('Technician Visit Delay', 'Technician Visit Delay'), ('Customer Support Issue', 'Customer Support Issue'), ('Other', 'Other')], max_length=60)),
                ('title', models.CharField(max_length=160)),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Urgent', 'Urgent')], default='Medium', max_length=20)),
                ('preferred_contact', models.CharField(choices=[('Phone', 'Phone'), ('Email', 'Email'), ('Either', 'Either')], default='Phone', max_length=20)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Technician Assigned', 'Technician Assigned'), ('Resolved', 'Resolved'), ('Closed', 'Closed')], default='Pending', max_length=30)),
                ('admin_note', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={'ordering': ['-created_at']},
        ),
    ]
