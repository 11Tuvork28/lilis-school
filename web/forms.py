from django import forms

class ContactForm(forms.Form):
    sender_name = forms.CharField(required=True,
     widget=forms.TextInput(attrs={'placeholder': 'Ihr name', 'type': 'text','class': 'form-control'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Ihre Email Adresse', 'type': 'email','class': 'form-control'}) )
    subject = forms.CharField(required=True,
    widget=forms.TextInput(attrs={'placeholder': 'Betreff', 'type': 'text','class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Sagen Sie uns was wir für Sie tun können', 'type': 'text','rows': '6', 'class': 'form-control'}), required=True)