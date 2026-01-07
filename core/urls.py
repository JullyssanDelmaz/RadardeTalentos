from django.urls import path
from .views import home_view, criar_aluno_view, redirect_pos_login, cadastro_view

urlpatterns = [
    path('', home_view, name='home'), 
    path('redirect/', redirect_pos_login, name='redirect'),
    path('aluno/criar/', criar_aluno_view, name='criar_aluno'),
    path('cadastro/', cadastro_view, name='cadastro'),
]