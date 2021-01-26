from django import forms
from Enrollments.models import Enrollment
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = "__all__"
