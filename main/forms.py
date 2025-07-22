from django import forms
from .models import Post, Comment, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'category']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class CategoryForm(forms.Form):
    category = forms.ChoiceField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        category = Category.objects.all()
        choices = [('', 'Все категории')] + [(c.id, c.name) for c in category]
        self.fields['category'].choices = choices
