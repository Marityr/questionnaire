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
        exclude = [
            'username', 
            'problem',
            'problem_two',
            'problem_fre',
            'problem_foo',
            'problem_fiv',
            'problem_sex',
            'problem_sev',
            'problem_ech',
            'problem_noi',
            'problem_thn',
            'problem_elv',
            'problem_lav',
            'problem_ulw',
            'problem_flv',
            'problem_fvt',
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Username',
            }),
            'age': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'placeholder': 'Age'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Male / female / other / .......'
            }),
            'massa': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Weight'
            }),
            'purpose': forms.Textarea(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'What are your goals on the way to improve your health?',
                'rows': '5'
            }),
            'decision': forms.Textarea(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Why did you decide to get screened by Welly?',
                'rows': '5'
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
            'problem_foo': forms.CheckboxInput(attrs={
                'name': 'problem_foo',
                'class': '',
            }),
            'problem_fiv': forms.CheckboxInput(attrs={
                'name': 'problem_fiv',
                'class': '',
            }),
            'problem_sex': forms.CheckboxInput(attrs={
                'name': 'problem_sex',
                'class': '',
            }),
            'problem_sev': forms.CheckboxInput(attrs={
                'name': 'problem_sev',
                'class': '',
            }),
            'problem_ech': forms.CheckboxInput(attrs={
                'name': 'problem_ech',
                'class': '',
            }),
            'problem_noi': forms.CheckboxInput(attrs={
                'name': 'problem_noi',
                'class': '',
            }),
            'problem_thn': forms.CheckboxInput(attrs={
                'name': 'problem_thn',
                'class': '',
            }),
            'problem_elv': forms.CheckboxInput(attrs={
                'name': 'problem_elv',
                'class': '',
            }),
            'problem_lav': forms.CheckboxInput(attrs={
                'name': 'problem_lav',
                'class': '',
            }),
            'problem_ulw': forms.CheckboxInput(attrs={
                'name': 'problem_ulw',
                'class': '',
            }),
            'problem_flv': forms.CheckboxInput(attrs={
                'name': 'problem_flv',
                'class': '',
            }),
            'problem_fvt': forms.CheckboxInput(attrs={
                'name': 'problem_fvt',
                'class': '',
            }),
        }
