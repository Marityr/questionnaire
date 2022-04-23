# from dataclasses import fields
from secrets import choice
from django import forms
from django.forms import ModelForm, TextInput, Textarea, FileInput, widgets, DateField
from .models import UserData
from django.forms import MultipleChoiceField, ChoiceField, Form



class UserDataForm(ModelForm):
    
    class Meta:
        model = UserData
        fields = '__all__'
        exclude = ['username']
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
            'problem': forms.CheckboxInput(attrs={
                'name': 'problem',
                'class': '',
            }),
            'problem_two': forms.CheckboxInput(attrs={
                'name': 'problem_two',

                'class': '',
            }),
            'problem_fre': forms.CheckboxInput(attrs={
                'name': 'problem_fre',
                'class': '',
            }),
        }
