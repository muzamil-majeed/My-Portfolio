from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name","email","subject","message"]

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5}),
        }

        error_messages = {
            'name': {
                'required': 'Please enter your name!',
                'max_length': 'Name is too long.',
            },
            'email': {
                'required': 'Please enter your email!',
                'invalid': 'Enter a valid email address.',
            },
            'subject': {
                'required': 'Please add a subject!',
            },
            'message': {
                'required': 'Please write your message!',
            },
        }