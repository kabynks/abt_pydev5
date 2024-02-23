from django.contrib.admin import *

from .models import *


@register(Tuition_language)
class TuitionLanguageAdmin(ModelAdmin):
    list_display = ("id", "language")
    list_display_links = ('id', 'language')


@register(Education_form)
class EducationFormAdmin(ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ('id', 'name')


@register(Subject)
class SubjectAdmin(ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ('id', 'name')
