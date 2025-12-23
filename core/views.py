from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .services import criar_aluno
from .models import Aluno
from .forms import AlunoForm

@login_required
def criar_aluno_view(request):
    
    if not (
        request.user.is_superuser or
        request.user.groups.filter(name='Escola').exists()
        ):
        return HttpResponseForbidden("Acesso negado")

    escola = request.user.escola

    form = AlunoForm(escola=escola)

    if request.method == 'POST':
        form = AlunoForm(request.POST, escola=escola)
        if form.is_valid():
            criar_aluno(form.cleaned_data, escola)
            return redirect('dashboard_escola')

    return render(request, 'core/criar_aluno.html', {'form':form})

def dashboard_redirect(user):
    if user.is_superuser:
        return 'admin:index'

    if user.groups.filter(name='Escola').exists():
        return 'dashboard_escola'

    if user.groups.filter(name='Aluno').exists():
        return 'dashboard_aluno'

    return 'dashboard_olheiro'

@login_required
def redirect_pos_login(request):
    return redirect(dashboard_redirect(request.user))