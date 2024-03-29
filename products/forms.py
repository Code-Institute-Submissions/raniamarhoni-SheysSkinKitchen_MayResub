from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Size, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class SizeForm(forms.ModelForm):

    class Meta:
        model = Size
        fields = ('sku', 'size', 'price', 'stock',)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('star', 'review',)
