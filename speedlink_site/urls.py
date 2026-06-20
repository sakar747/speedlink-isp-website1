from django.urls import include, path

urlpatterns = [
    path('', include('complaints.urls')),
]
