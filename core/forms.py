from django import forms
from core.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title', 'image', 'phone']

        widgets = {
            'title': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Ehtiyat hissəsinin adını daxil edin', 'class': 'part-input'}),
            'phone': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Əlaqə nömrənizi daxil edin', 'class': 'part-input'}),
            # 'car': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Adınızı daxil edin', 'class': 'input-product'}),
            # 'vin': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Soyadınızı daxil edin', 'class': 'input-product'}),
            # 'engine': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Soyadınızı daxil edin', 'class': 'input-product'}),
            # 'year': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Soyadınızı daxil edin', 'class': 'input-product'}),
            # 'body': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Soyadınızı daxil edin', 'class': 'input-product'}),
            # 'country': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Soyadınızı daxil edin', 'class': 'input-product'}),
            # 'transmission': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Soyadınızı daxil edin', 'class': 'input-product'}),
            # 'fuel': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Soyadınızı daxil edin', 'class': 'input-product'}),
            # 'turbo': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Soyadınızı daxil edin', 'class': 'input-product'}),
            # 'airbags': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Soyadınızı daxil edin', 'class': 'input-product'}),
            # 'image': forms.FileInput(attrs = {"id" : "image_field"})
        }