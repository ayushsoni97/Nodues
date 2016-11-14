from django.contrib import admin

from .models import Student
from .models import Choice

class ChoiceInLine(admin.StackedInline):
    model= Choice
    extra = 2

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['name']}),
    ]
    inlines = [ChoiceInLine]
admin.site.register(Student, StudentAdmin)
admin.site.register(Choice)
