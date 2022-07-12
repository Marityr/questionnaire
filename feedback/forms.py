# from dataclasses import fields
from secrets import choice
from django import forms
from django.forms import ModelForm, TextInput, Textarea, FileInput, widgets, DateField
from .models import Feedback
from django.forms import MultipleChoiceField, ChoiceField, Form



class FeedbackForm(ModelForm):
    
    class Meta:
        model = Feedback
        fields = '__all__'
        exclude = [
            'userID', 
            'email',
        ]
        widgets = {
            'rate': forms.Select(attrs={
                'class': 'form-control',
            }),
            'like': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'dislike': forms.Textarea(attrs={
                'class': 'form-control',
            }),
        }
