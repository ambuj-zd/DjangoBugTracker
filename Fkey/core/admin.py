from django.contrib import admin
from .models import Task , User , Role
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['userid','tasknum','title','status','details']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['userid','name','city',]

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name','role']
    



