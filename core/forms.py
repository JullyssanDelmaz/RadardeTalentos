from django import forms
from django.contrib.auth.models import User
from .models import Aluno, Time, CATEGORIAS, POSICOES


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

class observador_tecnicoForm(UserBaseForm):
    nome = forms.CharField(label="Nome Completo")
    celular = forms.CharField(label="Celular")
    cpf = forms.CharField(label="CPF")
    telefone = forms.CharField(label="Telefone")
    cargo = forms.CharField(label="Cargo/Função")
    clube = forms.CharField(label="Clube/Empresa")
    documento_identificacao = forms.FileField(label="Documento de Identificação", required=True)
    foto_perfil = forms.ImageField(label="Foto de Perfil", required=False)
    linkedin = forms.URLField(label="LinkedIn", required=False)
    certificacoes = forms.CharField(
        label="Certificações", 
        widget=forms.Textarea, 
        required=False
        )
    categorias_interesse = forms.MultipleChoiceField(
        choices=CATEGORIAS,
        widget=forms.CheckboxSelectMultiple,
        label="Categorias de Interesse",
        required=False
    )
    posicoes_preferenciais = forms.MultipleChoiceField(
        choices=POSICOES,
        widget=forms.CheckboxSelectMultiple,
        label="Posições Preferenciais",
        required=False
    )
    estado = forms.CharField(label="Estado", required=False)
    cidade = forms.CharField(label="Cidade", required=False)
    endereco = forms.CharField(label="Endereço", required=False)
    notificacoes = forms.BooleanField(label="Receber notificações", required=False)
    class Meta(UserBaseForm.Meta):
        fields = UserBaseForm.Meta.fields + [
            "nome",
            "cpf",
            "celular",
            "telefone",
            "cargo",
            "clube",
            "documento_identificacao",
            "foto_perfil",
            "linkedin",
            "certificacoes",
            "categorias_interesse",
            "posicoes_preferenciais",
            "estado",
            "cidade",
            "endereco",
            "notificacoes",
        ]