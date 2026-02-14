from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
    'name': forms.TextInput(attrs={
        # In portfolio/forms.py
'class': 'w-full p-3 bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-lg focus:outline-none focus:border-brand focus:ring-1 focus:ring-brand transition',
        'placeholder': 'John Doe'
    }),
    'email': forms.EmailInput(attrs={
        # In portfolio/forms.py
'class': 'w-full p-3 bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-lg focus:outline-none focus:border-brand focus:ring-1 focus:ring-brand transition',
        'placeholder': 'john@example.com'
    }),
    'message': forms.Textarea(attrs={
        # In portfolio/forms.py
'class': 'w-full p-3 bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-lg focus:outline-none focus:border-brand focus:ring-1 focus:ring-brand transition',
        'rows': 4,
        'placeholder': 'Tell me about your project...'
    }),
}