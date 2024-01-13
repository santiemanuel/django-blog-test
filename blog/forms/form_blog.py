from django import forms
from ..models import Post, Category
from martor.fields import MartorFormField

class PostForm(forms.ModelForm):
    content = MartorFormField()
    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }