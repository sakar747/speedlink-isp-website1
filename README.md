# SpeedLink Internet Services Website

## Project Title
**AI Chatbot-Based Complaint Management System for Local Internet Service Provider**

## What this project is
This is a normal ISP business website for **SpeedLink Internet Services** with complaint management and chatbot support features. Customers can browse services/packages, get troubleshooting help, submit complaints, track complaint status, and contact the ISP. Staff can log in to manage complaints.

## Main Features
- Home page using a blue and white ISP-style theme
- About page
- Services page
- Packages page
- Support / Troubleshooting page
- Smart ISP Assistant chatbot
- Submit Complaint page
- Unique complaint reference number generation
- Track Complaint page
- FAQ page
- Contact page with contact message storage
- Staff Login
- Admin Dashboard
- Complaint filtering by status/category/priority/search
- Complaint detail view
- Complaint status update with admin note

## Technology Stack
- Python
- Django
- MongoDB
- Official Django MongoDB Backend
- HTML
- CSS
- JavaScript

The project does not write direct PyMongo logic in the application views. MongoDB connection is configured through the Official Django MongoDB Backend in `settings.py`.

## Requirements
- Python 3.12 or later is recommended for the current 6.0.x Django MongoDB Backend package.
- MongoDB installed locally, or a MongoDB Atlas connection string.

## Setup: Windows
```bash
run_windows.bat
```

## Setup: macOS / Linux
```bash
./run_mac_linux.sh
```

## Manual Setup
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
copy .env.example .env        # Windows
# or
cp .env.example .env          # macOS/Linux

python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

Open:
```text
http://127.0.0.1:8000/
```

## MongoDB Configuration
Edit `.env`:

```env
MONGODB_URI=mongodb://localhost:27017
MONGODB_NAME=speedlink_isp_db
```

For MongoDB Atlas, replace `MONGODB_URI` with your Atlas connection string.

## Staff Login
```text
Username: admin
Password: admin123
```

You can change these in `.env`:
```env
STAFF_USERNAME=admin
STAFF_PASSWORD=admin123
```

## Suggested Demo Flow
1. Open Home page.
2. View Services and Packages.
3. Open Support / Troubleshooting.
4. Open Smart ISP Assistant.
5. Type: `My internet is not working`.
6. Show troubleshooting, category and priority suggestion.
7. Submit a complaint.
8. Save the generated reference number.
9. Track the complaint using the reference number.
10. Log in as staff.
11. Open dashboard and view complaint.
12. Update status to `Technician Assigned` or `Resolved`.
13. Track the complaint again to show updated status.

## Project Scope
Included in this prototype:
- Normal ISP website pages
- Complaint submission
- Complaint tracking
- Rule-based Smart ISP Assistant
- MongoDB complaint storage
- Staff complaint dashboard
- Status update workflow

Future improvements:
- Email/SMS notification
- Advanced AI chatbot model
- Customer login
- Technician account
- Payment integration
- File upload for evidence
- Analytics charts
