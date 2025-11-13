from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Subject, Grade, Attendance, LibraryItem, Notification, Task, ForumPost

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Usuário ou senha incorretos.")
    return render(request, "core/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            Profile.objects.create(user=user)
            login(request, user)
            return redirect("dashboard")
    return render(request, "core/register.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard_view(request):
    return render(request, "core/dashboard.html")

@login_required
def profile_view(request):
    profile = getattr(request.user, "profile", None)
    if request.method == "POST":
        # edição simples
        request.user.email = request.POST.get("email", request.user.email)
        request.user.save()
        if profile:
            profile.bio = request.POST.get("bio", profile.bio)
            profile.telefone = request.POST.get("telefone", profile.telefone)
            profile.save()
        messages.success(request, "Perfil atualizado.")
        return redirect("profile")
    return render(request, "core/profile.html", {"profile": profile})

@login_required
def assistant_view(request):
    return render(request, "core/assistant.html")

@login_required
def subjects_view(request):
    subjects = Subject.objects.all()
    return render(request, "core/subjects.html", {"subjects": subjects})

@login_required
def grades_view(request):
    grades = Grade.objects.filter(student=request.user)
    return render(request, "core/grades.html", {"grades": grades})

@login_required
def attendance_view(request):
    records = Attendance.objects.filter(student=request.user)
    return render(request, "core/attendance.html", {"records": records})

@login_required
def library_view(request):
    items = LibraryItem.objects.all()
    return render(request, "core/library.html", {"items": items})

@login_required
def notifications_view(request):
    notifs = Notification.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "core/notifications.html", {"notifs": notifs})

@login_required
def tasks_view(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, "core/tasks.html", {"tasks": tasks})

@login_required
def forum_view(request):
    posts = ForumPost.objects.all().order_by("-created_at")
    return render(request, "core/forum.html", {"posts": posts})

@login_required
def chatbot_view(request):
    return render(request, 'core/chatbot.html')