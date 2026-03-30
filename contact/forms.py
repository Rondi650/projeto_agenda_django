from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    # ------ CRIACAO --------
    # modo 1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        print('Print do attr: ', self.fields['first_name'].widget.attrs)

    # modo 2
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Novo placeholder'
            }
        ),
        # label='Seu primeiro nome',
        # help_text='Texto de ajuda para seu usuario'
    )

    # modo 3
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone', \
                 'email', 'description', 'category'
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'placeholder': 'Seu nome'})
        # }

    # ------ ERROS --------
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        print(cleaned_data)

        if first_name == last_name:
            msg = ValidationError(
                'Os nomes nao podem ser iguais',
                code='invalid')
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'abc':
            self.add_error(
                'first_name',
                ValidationError(
                    'Entrada invalida',
                    code='invalid'
                )
            )
        return first_name
