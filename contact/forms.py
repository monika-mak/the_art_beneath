from django import forms
from .models import ContactRequest, Art  # Import Art model

class ContactRequestForm(forms.ModelForm):

    QUERY_CHOICES = [
        ('general', 'General Query'),
        ('size', 'Size Query')
    ]

    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'art', 'custom_size', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'custom_size': forms.TextInput(attrs={'placeholder': 'Enter custom size (optional)'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['art'].empty_label = "Select an artwork (optional)"  # Adds a placeholder-like option




