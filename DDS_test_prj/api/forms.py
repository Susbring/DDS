from django import forms

from .models import FinancialMove


class DDSForm(forms.ModelForm):
    class Meta:
        model = FinancialMove
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
        }
