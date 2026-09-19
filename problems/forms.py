from django import forms
from .models import Problem, ProblemAssignment
from accounts.models import Department


class ProblemForm(forms.ModelForm):

    class Meta:
        model = Problem
        fields = [
            'category',
            'title',
            'description',
            'photo',
            'location',
        ]


class ProblemAssignmentForm(forms.ModelForm):

    class Meta:
        model = ProblemAssignment
        fields = [
            'department',
        ]