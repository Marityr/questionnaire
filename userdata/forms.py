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
            'problem_4': forms.CheckboxInput(attrs={
                'name': 'problem_4',
                'class': '',
            }),
            'problem_5': forms.CheckboxInput(attrs={
                'name': 'problem_5',
                'class': '',
            }),
            'problem_6': forms.CheckboxInput(attrs={
                'name': 'problem_6',
                'class': '',
            }),
            'problem_7': forms.CheckboxInput(attrs={
                'name': 'problem_7',
                'class': '',
            }),
            'problem_8': forms.CheckboxInput(attrs={
                'name': 'problem_8',
                'class': '',
            }),
            'problem_9': forms.CheckboxInput(attrs={
                'name': 'problem_9',
                'class': '',
            }),
            'problem_10': forms.CheckboxInput(attrs={
                'name': 'problem_10',
                'class': '',
            }),
            'problem_11': forms.CheckboxInput(attrs={
                'name': 'problem_11',
                'class': '',
            }),
            'problem_12': forms.CheckboxInput(attrs={
                'name': 'problem_12',
                'class': '',
            }),
            'problem_13': forms.CheckboxInput(attrs={
                'name': 'problem_13',
                'class': '',
            }),
            'problem_14': forms.CheckboxInput(attrs={
                'name': 'problem_14',
                'class': '',
            }),
            'problem_15': forms.CheckboxInput(attrs={
                'name': 'problem_15',
                'class': '',
            }),
        }
