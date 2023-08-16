from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Название товара'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Описание товара'}))
    price = forms.FloatField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    count = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField()
