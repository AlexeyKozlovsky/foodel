from django import forms

from core.models import ClientRequest


class ClientRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientRequestForm, self).__init__(*args, **kwargs)
        self.fields['bank'].empty_label = 'Выберите банк'

    class Meta:
        model = ClientRequest
        fields = ['email', 'phone', 'first_name', 'last_name',
                  'name', 'description', 'img', 'address',
                  'employees_count', 'employee_money',
                  'account_num', 'corr_account_num', 'TIN_num', 'bank']
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
            'employees_count': forms.TextInput(attrs={
                'class': 'input-primary data-block-input',
                'placeholder': 'Количество сотрудников'
            }),
            'employee_money': forms.TextInput(attrs={
                'class': 'input-primary data-block-input',
                'placeholder': 'Средства на сотрудника в месяц'
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
