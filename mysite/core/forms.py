from django import forms
from .models import Job
from .models import Note
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields ='__all__'
        widgets = {
            'position': forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded'
            }),
            'company': forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded'

            }),
            'date_applied': forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded'

            }),
            'status': forms.Select(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded'

            }),
        }