from django.urls import path
from .views import criar_aluno_view, redirect_pos_login

urlpatterns = [
    path('redirect/', redirect_pos_login, name='redirect'),
    path('aluno/criar/', criar_aluno_view, name='criar_aluno'),
]