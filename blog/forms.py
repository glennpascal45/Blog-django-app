from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'status', 'body', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'post title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'rows': 10}),

        }



