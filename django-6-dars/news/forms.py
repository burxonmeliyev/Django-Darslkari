from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ismingiz'}),
            'content': forms.Textarea(attrs={'placeholder': 'Izohingizni yozing...', 'rows': 3}),
        }