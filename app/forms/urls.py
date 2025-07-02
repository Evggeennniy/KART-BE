from django.urls import path
from forms.views import ApplicationFormView

urlpatterns = [
    path('application/', ApplicationFormView.as_view(), name='application-form-create'),
]
