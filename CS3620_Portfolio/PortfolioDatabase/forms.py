from django import forms
from .models import Portfolio, Hobby, Contact

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['project_name', 'project_desc', 'project_image']

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['hobby_name', 'hobby_desc', 'hobby_image']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_email', 'contact_message']
