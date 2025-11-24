from django.urls import path
from . import views

urlpatterns = [
    # raiz do site vai para login
    path("", views.login_view, name="login"),

    # LOGIN / LOGOUT
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("cadastro/aluno/", views.cadastro_aluno, name="cadastro_aluno"),
    path("cadastro/professor/", views.cadastro_professor, name="cadastro_professor"),

    # ALUNO
    path("aluno/dashboard/", views.aluno_dashboard, name="aluno_dashboard"),
    path("aluno/notas/", views.aluno_notas, name="aluno_notas"),
    path("aluno/faltas/", views.aluno_faltas, name="aluno_faltas"),
    path("aluno/biblioteca/", views.aluno_biblioteca, name="aluno_biblioteca"),
    path("aluno/tarefas/", views.aluno_tarefas, name="aluno_tarefas"),
    path("aluno/notificacoes/", views.aluno_notificacoes, name="aluno_notificacoes"),
    path("aluno/forum/", views.aluno_forum, name="aluno_forum"),
    path("aluno/perfil/", views.aluno_perfil, name="aluno_perfil"),

    # PROFESSOR
    path("professor/dashboard/", views.professor_dashboard, name="professor_dashboard"),
    path("professor/turmas/", views.prof_turmas, name="prof_turmas"),
    path("professor/presenca/", views.prof_presenca, name="prof_presenca"),
    path("professor/notas/", views.prof_notas, name="prof_notas"),
    path("professor/biblioteca/", views.prof_biblioteca, name="prof_biblioteca"),
    path("professor/tarefa/", views.prof_tarefa, name="prof_tarefa"),
    path("professor/forum/", views.prof_forum, name="prof_forum"),
    path("professor/perfil/", views.prof_perfil, name="prof_perfil"),

    # CHATBOT
    path("chatbot/", views.chatbot_page, name="chatbot_page"),
    path("api/chatbot/", views.chatbot_api, name="chatbot_api"),
]
