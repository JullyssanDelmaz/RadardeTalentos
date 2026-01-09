from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home_view, criar_aluno_view, redirect_pos_login, cadastro_view, dashboard
urlpatterns = [
    path('', home_view, name='home'), 
    path('pos_login/', redirect_pos_login, name='pos_login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('aluno/criar/', criar_aluno_view, name='criar_aluno'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]