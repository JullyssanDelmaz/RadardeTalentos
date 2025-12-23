from django.db import models

from django.contrib.auth.models import User

class Escola(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

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


class Olheiro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username