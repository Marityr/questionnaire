# from dataclasses import fields
from secrets import choice
from django import forms
from django.forms import ModelForm, TextInput, Textarea, FileInput, widgets, DateField
from .models import UserData


class UserDataForm(ModelForm):
    
    class Meta:
        model = UserData
        fields = '__all__'
        exclude = ['username']
        queryset= [
            'age',
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Username',
            }),
            'age': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Age'
            }),
            'gender': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Male/female'
            }),
            'massa': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Weight'
            }),
            'purpose': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'What are your goals on the way to improve your health?'
            }),
            'decision': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Why did you decide to get screened by Welly?'
            }),
            'problem': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Which of health problems do you have?'
            }),
        }
