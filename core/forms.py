from django import forms
from core.models import ContactMessage, Donation

# Contact form
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model  = ContactMessage
        fields = '__all__'

# Dontation form
class DonationForm(forms.ModelForm):
    class Meta:
        model  = Donation
        fields = '__all__'
