from django import forms

from vocabulator.words.models import Definition


class DefinitionInlineForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 100}))
    example = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 100}), required=False)
    translate = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 100}), required=False)
    synonyms = forms.CharField(widget=forms.TextInput(attrs={'size': 102}), required=False, help_text="Слова синонимы через запятую")

    class Meta:
        model = Definition
        fields = "__all__"


class ExampleInlineForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 100}), required=False)
    translate = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 100}), required=False)

    class Meta:
        model = Definition
        fields = "__all__"
