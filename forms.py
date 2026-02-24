from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Inspection

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['reference', 'title', 'inspection_type', 'status', 'inspector_id', 'inspection_date', 'result', 'notes']
        widgets = {
            'reference': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'title': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'inspection_type': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'status': forms.Select(attrs={'class': 'select select-sm w-full'}),
            'inspector_id': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'inspection_date': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'date'}),
            'result': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'notes': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 3}),
        }

