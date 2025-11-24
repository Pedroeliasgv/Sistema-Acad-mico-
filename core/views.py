from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import AlunoSignUpForm, ProfessorSignUpForm

User = get_user_model()

# --------------------- LOGIN/LOGOUT ---------------------

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        tipo = request.POST.get("tipo")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Usuário ou senha incorretos.")
            return render(request, "core/login.html", {"username": username})

        if tipo == "aluno" and not user.is_aluno:
            messages.error(request, "Este usuário não é aluno.")
            return render(request, "core/login.html", {"username": username})
        if tipo == "professor" and not user.is_professor:
            messages.error(request, "Este usuário não é professor.")
            return render(request, "core/login.html", {"username": username})

        login(request, user)

        if user.is_aluno:
            return redirect("aluno_dashboard")
        else:
            return redirect("professor_dashboard")

    return render(request, "core/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


# --------------------- CADASTRO ---------------------

def cadastro_aluno(request):
    if request.method == "POST":
        form = AlunoSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_aluno = True
            user.save()
            messages.success(request, "Aluno cadastrado com sucesso.")
            login(request, user)
            return redirect("aluno_dashboard")
        else:
            messages.error(request, "Verifique os dados do formulário.")
    else:
        form = AlunoSignUpForm()
    return render(request, "core/cadastro_aluno.html", {"form": form})


def cadastro_professor(request):
    if request.method == "POST":
        form = ProfessorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_professor = True
            user.save()
            messages.success(request, "Professor cadastrado com sucesso.")
            login(request, user)
            return redirect("professor_dashboard")
        else:
            messages.error(request, "Verifique os dados do formulário.")
    else:
        form = ProfessorSignUpForm()
    return render(request, "core/cadastro_professor.html", {"form": form})


# --------------------- DASHBOARDS ---------------------

@login_required
def aluno_dashboard(request):
    if not request.user.is_aluno:
        return redirect("login")
    return render(request, "core/aluno_dashboard.html")


@login_required
def professor_dashboard(request):
    if not request.user.is_professor:
        return redirect("login")
    return render(request, "core/professor_dashboard.html")


# --------------------- ALUNO ---------------------

@login_required
def aluno_notas(request):
    return render(request, "core/aluno_notas.html")

@login_required
def aluno_faltas(request):
    return render(request, "core/aluno_faltas.html")

@login_required
def aluno_biblioteca(request):
    return render(request, "core/aluno_biblioteca.html")

@login_required
def aluno_tarefas(request):
    return render(request, "core/aluno_tarefas.html")

@login_required
def aluno_notificacoes(request):
    return render(request, "core/aluno_notificacoes.html")

@login_required
def aluno_forum(request):
    return render(request, "core/aluno_forum.html")

@login_required
def aluno_perfil(request):
    return render(request, "core/aluno_perfil.html")


# --------------------- PROFESSOR ---------------------

@login_required
def prof_turmas(request):
    return render(request, "core/prof_turmas.html")

@login_required
def prof_presenca(request):
    return render(request, "core/prof_presenca.html")

@login_required
def prof_notas(request):
    return render(request, "core/prof_notas.html")

@login_required
def prof_biblioteca(request):
    return render(request, "core/prof_biblioteca.html")

@login_required
def prof_tarefa(request):
    return render(request, "core/prof_tarefa.html")

@login_required
def prof_forum(request):
    return render(request, "core/prof_forum.html")

@login_required
def prof_perfil(request):
    return render(request, "core/prof_perfil.html")


# --------------------- CHATBOT ---------------------

def chatbot_page(request):
    return render(request, "core/chatbot.html")


@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        import json
        body = json.loads(request.body)
        question = body.get("message", "")
        # Resposta simulada sem depender de IA externa
        answer = f"Resposta simulada para: {question}"
        return JsonResponse({"answer": answer})
