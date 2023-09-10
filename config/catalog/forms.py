from django import forms
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

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
