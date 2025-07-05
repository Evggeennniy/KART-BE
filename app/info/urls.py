# urls.py

from django.urls import path
from info.views import FAQListView

urlpatterns = [
    path('faqs/', FAQListView.as_view(), name='faq-list'),
]
