from django import forms
from django.forms.widgets import NumberInput
import datetime

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
class FormClass(forms.Form):
    name=forms.CharField(label="enter name")
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email=forms.CharField(label="enter email")
    agree = forms.BooleanField(initial=True)
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    email_address = forms.EmailField( 
    required = False,)
    message = forms.CharField(
	max_length = 10,
    )
    first_name = forms.CharField(initial='Your name')
    day = forms.DateField(initial=datetime.date.today)
    # favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    # favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    # root='django_Form'