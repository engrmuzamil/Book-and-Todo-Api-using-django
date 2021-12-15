from django.contrib import admin
from .models import Todo
# Register your models here.
class TodoAdminView(admin.ModelAdmin):
    list_display = ('id','title', 'details')

admin.site.register(Todo, TodoAdminView)