from django.contrib import admin

from .models import Escola, Time, Aluno, Observador_tecnico

admin.site.register(Escola)
admin.site.register(Time)
admin.site.register(Aluno)
admin.site.register(Observador_tecnico)
