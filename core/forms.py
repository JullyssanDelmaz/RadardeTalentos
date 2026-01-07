from django import forms
from django.contrib.auth.models import User
from .models import Aluno, Time


# ----------------------
# Form base de usuário
# ----------------------
class UserBaseForm(forms.ModelForm):
    username = forms.CharField(label="Nome de Usuário")
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Senha")
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


# ----- ESCOLA ----- 

class EscolaForm(UserBaseForm):
    nome = forms.CharField(label="Nome da Escola")
    diretor = forms.CharField(label="Diretor")
    cnpj = forms.CharField(label="CNPJ")
    razao_social = forms.CharField(label="Razão Social")
    cidade = forms.CharField(label="Cidade")
    celular = forms.CharField(label="Celular")
    telefone = forms.CharField(label="Telefone")


    class Meta(UserBaseForm.Meta):
        fields = UserBaseForm.Meta.fields + [
            'nome',
            'diretor',
            'cnpj',
            'razao_social',
            'cidade',
            'telefone',
            'celular',
        ]

class OlheiroForm(UserBaseForm):
    nome = forms.CharField(label="Nome Completo")
    cpf = forms.CharField(label="CPF")
    telefone = forms.CharField(label="telefone")
    time = forms.CharField(label="Time")
    class Meta(UserBaseForm.Meta):
        fields = UserBaseForm.Meta.fields + [
            "nome",
            "cpf",
            "telefone",
            "time",
        ]