from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("profile/", views.profile_view, name="profile"),
    path("assistant/", views.assistant_view, name="assistant"),
    path("subjects/", views.subjects_view, name="subjects"),
    path("grades/", views.grades_view, name="grades"),
    path("attendance/", views.attendance_view, name="attendance"),
    path("library/", views.library_view, name="library"),
    path("notifications/", views.notifications_view, name="notifications"),
    path("tasks/", views.tasks_view, name="tasks"),
    path("forum/", views.forum_view, name="forum"),
    path("chatbot/", views.chatbot_view, name="chatbot"),
]
