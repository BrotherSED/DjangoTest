from .models import News_table
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, NumberInput


class News_tableForm(ModelForm):
    class Meta:
        model = News_table
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            "anons": TextInput(attrs={'class': 'form-control', 'placeholder': 'Анонс статьи'}),
            "date": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
            "full_text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст статьи'})
        }
