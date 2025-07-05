from django.urls import path
from forms.views import ApplicationFormView, DealerApplicationCreateView, InstructorApplicationFormView

urlpatterns = [
    path('application/', ApplicationFormView.as_view(), name='application-form-create'),
    path('dealer-applications/', DealerApplicationCreateView.as_view(), name='dealer-application-create'),
    path('instructor-applications/', InstructorApplicationFormView.as_view(), name='instructor-application-create'),
]
