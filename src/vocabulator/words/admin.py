from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from vocabulator.words.models import Category, Word


class HasTranslationFilter(SimpleListFilter):
    title = 'Has translation'
    parameter_name = 'has_translation'

    def lookups(self, request, model_admin):
        return ("yes", "Yes"), ("no", "No"),

    def queryset(self, request, queryset):
        if self.value() == "yes":
            return queryset.exclude(translation="")
        elif self.value() == "no":
            return queryset.filter(translation="")
        else:
            return queryset


@admin.register(Word)
class WordsAdmin(admin.ModelAdmin):
    list_filter = "category", HasTranslationFilter,
    list_display = "name", "has_translation", "category",

    def has_translation(self, obj):
        return "+" if obj.has_translation else "-"


admin.site.register(Category)
