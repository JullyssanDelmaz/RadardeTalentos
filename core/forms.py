from django import forms
from django.contrib.auth.models import User
from .models import Aluno, Time


# ----------------------
# Form base de usuário
# ----------------------
class UserBaseForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# ----------------------
# Criar aluno
# ----------------------
class AlunoForm(UserBaseForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    time = forms.ModelChoiceField(
        queryset=Time.objects.none()
    )

    class Meta(UserBaseForm.Meta):
        fields = UserBaseForm.Meta.fields + ['data_nascimento', 'time']

    def __init__(self, *args, **kwargs):
        escola = kwargs.pop('escola', None)
        super().__init__(*args, **kwargs)

        if escola:
            self.fields['time'].queryset = Time.objects.filter(escola=escola)