from django.contrib.auth.models import User, Group
from .models import Escola, Aluno, Observador_tecnico, Time

def criar_escola(dados):
    user = User.objects.create_user(
        username=dados['username'],
        password=dados['password'],
        email=dados.get('email', '')
    )

    escola = Escola.objects.create(
        user=user,
        nome=dados['nome'],
        cidade=dados['cidade']
    )

    user.groups.add(Group.objects.get(name='Escola'))
    return escola


def criar_aluno(dados, escola):
    user = User(
        username=dados['username'],
        email=dados.get('email', '')
    )
    user.set_password(dados['password'])
    user.save()

    aluno = Aluno.objects.create(
        user=user,
        escola=escola,
        time=dados['time'],
        data_nascimento=dados['data_nascimento']
    )

    user.groups.add(Group.objects.get(name='Aluno'))
    return aluno


def criar_observador_tecnico(dados):
    user = Observador_tecnico.objects.create_user(
        username=dados['username'],
        password=dados['password']
    )

    observador_tecnico = Observador_tecnico.objects.create(
        user=user,
        clube=dados.get('clube', '')
    )

    user.groups.add(Group.objects.get(name='Observador_tecnico'))
    return observador_tecnico
