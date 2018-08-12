from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from vocabulator.words.forms import DefinitionInlineForm, ExampleInlineForm
from vocabulator.words.models import Category, Word, Definition, Kanji, Example, Language


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


class DefinitionInline(admin.StackedInline):
    model = Definition
    extra = 0
    form = DefinitionInlineForm


class ExampleInline(admin.StackedInline):
    model = Example
    extra = 0
    form = ExampleInlineForm


class KanjiInline(admin.TabularInline):
    model = Kanji
    extra = 0


@admin.register(Word)
class WordsAdmin(admin.ModelAdmin):
    list_filter = "category", HasTranslationFilter, "need_clarify",
    list_display = "name", "has_translation", "category",
    exclude = "score",
    search_fields = "name", "translation"
    inlines = [
        ExampleInline,
        DefinitionInline,
        KanjiInline
    ]

    def has_translation(self, obj):
        return "+" if obj.has_translation else "-"


admin.site.register(Category)
admin.site.register(Language)
