from django.contrib import admin

from .models import Escola, Time, Aluno, observador_tecnico

admin.site.register(Escola)
admin.site.register(Time)
admin.site.register(Aluno)
admin.site.register(observador_tecnico)
