from django import forms

class MyForm(forms.Form):
    my_variable = forms.CharField(label='SQLクエリ')
