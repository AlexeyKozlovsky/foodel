from django import forms

from core.models import MarketRequest


class PartnerRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PartnerRequestForm, self).__init__(*args, **kwargs)
        self.fields['bank'].empty_label = 'Выберите банк'

    class Meta:
        model = MarketRequest
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'input-primary data-block-input',
                'placeholder': 'Email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'input-primary data-block-input',
                'placeholder': 'Телефон'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'input-primary data-block-input',
                'placeholder': 'Имя'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'input-primary data-block-input',
                'placeholder': 'Фамилия'
            }),
            'name': forms.TextInput(attrs={
                'class': 'input-primary data-block-input',
                'placeholder': 'Название компании'
            }),
            'description': forms.TextInput(attrs={
                'class': 'input-primary data-block-input',
                'placeholder': 'Описание компании'
            }),
            'img': forms.FileInput(attrs={
                'id': 'img-input',
                'class': 'input-primary data-block-input file-input'
            }),
            'address': forms.TextInput(attrs={
                'class': 'input-primary data-block-input',
                'placeholder': 'Адрес'
            }),
            'categories': forms.SelectMultiple(attrs={
                'class': 'input-primary data-block-input',
            }),
            'account_num': forms.TextInput(attrs={
                'class': 'input-primary data-block-input',
                'placeholder': 'Номер счёта'
            }),
            'TIN_num': forms.TextInput(attrs={
                'class': 'input-primary data-block-input',
                'placeholder': 'ИНН'
            }),
            'corr_account_num': forms.TextInput(attrs={
                'class': 'input-primary data-block-input',
                'placeholder': 'Корр. счёт'
            }),
            'bank': forms.Select(attrs={
                'class': 'input-primary data-block-input',
            })
        }
