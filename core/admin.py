from django.contrib import admin
from .models import Profile, Subject, Grade, Attendance, LibraryItem, Notification, Task, ForumPost

admin.site.register(Profile)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Attendance)
admin.site.register(LibraryItem)
admin.site.register(Notification)
admin.site.register(Task)
admin.site.register(ForumPost)
