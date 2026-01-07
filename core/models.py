from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


CATEGORIAS = (
    ('SUB7', 'Sub-7'), 
    ('SUB8', 'Sub-8'), 
    ('SUB9', 'Sub-9'), 
    ('SUB11', 'Sub-11'), 
    ('SUB13', 'Sub-13'), 
    ('SUB15', 'Sub-15'), 
    ('SUB17', 'Sub-17'), 
    ('SUB20', 'Sub-20'),
)
POSICOES = (
    ('GOL', 'Goleiro'), 
    ('LD', 'Lateral Direito'), 
    ('LE', 'Lateral Esquerdo'), 
    ('ZAG', 'Zagueiro'), 
    ('VOL', 'Volante'),
    ('AD', 'Ala Direito'),
    ('AE', 'Ala Esquerdo'), 
    ('MC', 'Meia/Meia Central'),
    ('MLE', 'Meia Lateral Esquerdo'),
    ('MLD', 'Meia Lateral Direito'),
    ('MAD', 'Meia Atacante Direito'), 
    ('MAE', 'Meia Atacante Esquerdo'), 
    ('ATA', 'Atacante'),
    ('CA', 'Centroavante'), 
    ('PON', 'Ponta'),
)

class Escola(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, default="")
    diretor = models.CharField(max_length=100, default="")
    cnpj = models.CharField(max_length=18, default="")
    razao_social = models.CharField(max_length=250, default="")
    telefone = models.CharField(max_length=11, default="")
    celular = models.CharField(max_length=12, default="")
    cidade = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.nome


class Time(models.Model):
    escola = models.ForeignKey(
        Escola,
        on_delete=models.CASCADE,
        related_name='times'
    )
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.escola.nome}"


class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    escola = models.ForeignKey(
        Escola,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    time = models.ForeignKey(
        Time,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    data_nascimento = models.DateField()

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class observador_tecnico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=150)
    celular = models.CharField(max_length=20)
    cargo = models.CharField(max_length=150)
    clube = models.CharField(max_length=150)
    documento_identificacao = models.FileField(
        upload_to = 'documentos_observador_tecnico/',
        verbose_name = "Documento de Identificação"
    )

    foto_perfil = models.ImageField(
        upload_to = 'fotos_observador_tecnico/',
        blank=True,
        null=True
    )
    linkedin = models.URLField(blank=True, null=True)
    certificacoes = models.TextField(
        blank=True, 
        verbose_name="Certificações"
    )
    certificacoes_arquivo = models.FileField(
        upload_to='certificacoes_observador_tecnico/',
        blank=True,
        verbose_name="Comprovante de Certificações"
    )

    estado = models.CharField(max_length=150, blank=True)
    cidade = models.CharField(max_length=150, blank=True)
    endereco = models.CharField(max_length=150, blank=True)
    telefone = models.CharField(max_length=11, default="")
    notificacoes = models.BooleanField(default=True)
    categorias_interesse = MultiSelectField(
        choices=CATEGORIAS,
        max_length=100,
        verbose_name="Categorias de Interesse",
        blank=True
    )
    posicoes_preferenciais = MultiSelectField(
        choices=POSICOES,
        max_length=50,
        verbose_name="Posições Preferenciais",
        blank=True
    )
    

    def __str__(self):
        return self.user.get_full_name() or self.user.username