from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .services import criar_aluno
from .models import Aluno, Escola, Observador_tecnico
from .forms import AlunoForm, EscolaForm, Observador_tecnicoForm
from django.contrib.auth.models import Group

def  home_view(request):
    return render(request, 'core/home.html')



def cadastro_view(request):
    escola_form = EscolaForm(
        request.POST or None,
        request.FILES or None, 
        prefix="escola")
    
    observador_tecnico_form = Observador_tecnicoForm(
        request.POST or None,
        request.FILES or None, 
        prefix="observador_tecnico"
    )

    if request.method == "POST":
        tipo = request.POST.get("tipo")
    
        if tipo == "Escola" and escola_form.is_valid():
            user = escola_form.save(commit=False)
            password = escola_form.cleaned_data["password"]
            user.set_password(password)
            user.save()

            grupo = Group.objects.get(name="Escola")
            user.groups.add(grupo)
        
            Escola.objects.create(
                user=user, 
                nome=escola_form.cleaned_data["nome"], 
                diretor=escola_form.cleaned_data["diretor"], 
                cnpj=escola_form.cleaned_data["cnpj"], 
                razao_social=escola_form.cleaned_data["razao_social"], 
                telefone=escola_form.cleaned_data["telefone"], 
                celular=escola_form.cleaned_data["celular"], 
                cidade=escola_form.cleaned_data["cidade"],
            )
            return redirect("home")


        if tipo == "Observador_tecnico" and observador_tecnico_form.is_valid():
            user = observador_tecnico_form.save(commit=False)
            password = observador_tecnico_form.cleaned_data["password"]
            user.set_password(password)
            user.save()

            grupo = Group.objects.get(name="Observador Técnico")
            user.groups.add(grupo)

            Observador_tecnico.objects.create(
                user=user, 
                nome=observador_tecnico_form.cleaned_data["nome"], 
                cpf=observador_tecnico_form.cleaned_data["cpf"], 
                celular=observador_tecnico_form.cleaned_data["celular"], 
                cargo=observador_tecnico_form.cleaned_data["cargo"], 
                clube=observador_tecnico_form.cleaned_data["clube"], 
                documento_identificacao=observador_tecnico_form.cleaned_data["documento_identificacao"], 
                foto_perfil=observador_tecnico_form.cleaned_data["foto_perfil"], 
                linkedin=observador_tecnico_form.cleaned_data["linkedin"], 
                certificacoes=observador_tecnico_form.cleaned_data["certificacoes"], 
                certificacoes_arquivo=observador_tecnico_form.cleaned_data["certificacoes_arquivo"], 
                estado=observador_tecnico_form.cleaned_data["estado"], 
                cidade=observador_tecnico_form.cleaned_data["cidade"],
                telefone=observador_tecnico_form.cleaned_data["telefone"], 
                notificacoes=observador_tecnico_form.cleaned_data["notificacoes"], 
                categorias_interesse=observador_tecnico_form.cleaned_data["categorias_interesse"], 
                posicoes_preferenciais=observador_tecnico_form.cleaned_data["posicoes_preferenciais"],
            )

            return redirect("home")
    return render(request, "core/cadastro.html", {
        "escola_form": escola_form, 
        "observador_tecnico_form":observador_tecnico_form,
        })

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

    return 'dashboard_observador_tecnico'

@login_required
def redirect_pos_login(request):
    return redirect(dashboard_redirect(request.user))