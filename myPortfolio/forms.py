from django import forms
from myPortfolio.models import ContactUsInfo

class ContactUsForm(forms.ModelForm):
    message = forms.CharField( widget=forms.Textarea(attrs={'overflow-y': 'scroll','style':'resize:none;'}) )
    class Meta:
        model = ContactUsInfo
        fields = "__all__"