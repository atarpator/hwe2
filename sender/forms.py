from django import forms
from sender.models import EmailSender

class EmailSenderForm(forms.ModelForm):

    email = forms.CharField(
        label='Адрес электронной почты',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'class': 'form-control',
            }
        )
    )

    subject = forms.CharField(
        label='Тема',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'type': 'text',
                'class': 'form-control',
            }
        )
    )

    message = forms.CharField(
        label='Текст сообщения',
        widget=forms.Textarea(
            attrs={
                'required': True,
                'type': 'text',
                'class': 'form-control',
            }
        )
    )

    

    delay = forms.IntegerField(
        label='Задержка отправки в секундах',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'type': 'number',
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = EmailSender
        fields = ('email', 'subject', 'message', 'delay')
