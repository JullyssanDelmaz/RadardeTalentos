from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .services import criar_aluno
from .models import Aluno, Escola
from .forms import AlunoForm, EscolaForm, OlheiroForm
from django.contrib.auth.models import Group

def  home_view(request):
    return render(request, 'core/home.html')



def cadastro_view(request):
    escola_form = EscolaForm(request.POST or None, prefix="escola")
    olheiro_form = OlheiroForm(request.POST or None, prefix="olheiro")

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
            return redirect("login")


        if tipo == "Olheiro" and olheiro_form.is_valid():
            user = olheiro_form.save(commit=False)
            password = olheiro_form.cleaned_data["password"]
            user.set_password(password)
            user.save()

            grupo = Group.objects.get(name="Olheiro")
            user.groups.add(grupo)

            return redirect("login")
    return render(request, "core/cadastro.html", {
        "escola_form": escola_form, 
        "olheiro_form":olheiro_form,
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

    return 'dashboard_olheiro'

@login_required
def redirect_pos_login(request):
    return redirect(dashboard_redirect(request.user))