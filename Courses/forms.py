from django import forms
from Courses.models import Course
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
