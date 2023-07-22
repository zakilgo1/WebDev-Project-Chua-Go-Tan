from django import forms
from .models import Quotation

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ['Pen_count', 'Eraser_count', 'Notebook_count', 'Stapler_count', 'Calculator_count']