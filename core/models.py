from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_professor = models.BooleanField(default=False)
    is_aluno = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Profile(models.Model):
    TIPO_USUARIO = (
        ("aluno", "Aluno"),
        ("professor", "Professor"),
    )

    user = models.OneToOneField("core.CustomUser", on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to="profiles/", blank=True, null=True)
    tipo = models.CharField(max_length=10, choices=TIPO_USUARIO, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.tipo}"


class Subject(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Grade(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey("core.CustomUser", on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=5, decimal_places=2)


class Attendance(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)
    student = models.ForeignKey("core.CustomUser", on_delete=models.CASCADE)


class LibraryItem(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120, blank=True)
    file = models.FileField(upload_to="library/", blank=True, null=True)

    def __str__(self):
        return self.title


class Notification(models.Model):
    user = models.ForeignKey("core.CustomUser", on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)
    assigned_to = models.ForeignKey("core.CustomUser", on_delete=models.CASCADE)


class ForumPost(models.Model):
    author = models.ForeignKey("core.CustomUser", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
