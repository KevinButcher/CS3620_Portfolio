from django import forms
from .models import Portfolio, Hobby, Contact, Tag

class PortfolioForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = Portfolio
        fields = ['project_name', 'project_desc', 'project_image', 'project_url', 'project_video', 'tags']

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['hobby_name', 'hobby_desc', 'hobby_image']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_email', 'contact_subject', 'contact_message']
