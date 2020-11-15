from django import forms

class HomeForm(forms.Form):
    product_list = forms.URLField(max_length=225)
    aa = forms.FileField(max_length=225)