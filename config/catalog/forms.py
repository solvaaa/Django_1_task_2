from django import forms
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def check_restricted_words(self, text):
        restricted_words = [
            'казино',
            'криптовалюта',
            'крипта',
            'биржа',
            'дешево',
            'бесплатно',
            'обман',
            'полиция',
            'радар']
        for word in restricted_words:
            if word in text.lower():
                return True
            return False

    def clean_name(self):
        name = self.cleaned_data['name']

        if self.check_restricted_words(name):
            raise forms.ValidationError('Запрещенное слово в названии товара')

        return name

    def clean_description(self):
        description = self.cleaned_data['description']

        if self.check_restricted_words(description):
            raise forms.ValidationError('Запрещенное слово в описании товара')

        return description

class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__()
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'from-check'
