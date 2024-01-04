from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name','email','text']
        # exclude = ['text'] seçilmeyen fields
        labels = {
            'full_name':'Ad Soyad',
            'email':'Eposta',
            'text':'Yorum',
        }
        widgets  = {
            'full_name':forms.TextInput(attrs={'class':'form-control bg-light','placeholder':'Adınızı Girin'}),
            'email':forms.EmailInput(attrs={'class':'form-control bg-light','placeholder':'Eposta Adresini Girin'}),
            'text':forms.Textarea(attrs={'class':'form-control bg-light text-black','placeholder':'Yorum Yaz'}),
        }