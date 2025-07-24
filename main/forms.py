from django import forms
from .models import Post, Comment, Category


class PostForm(forms.ModelForm):
    '''
    Форма создания поста

    функция init используется для bootstap и styles.css
    '''
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            input_type = getattr(field.widget, 'input_type', None)
            if input_type != 'file':
                field.widget.attrs.update({'class': 'form-control'})
            else:
                field.widget.attrs.update({'class': 'form-control-file'})


class CommentForm(forms.ModelForm):
    '''
    Форма для возможности оставить комментарии
    '''
    class Meta:
        model = Comment
        fields = ['text']


class CategoryForm(forms.Form):
    '''
    Форма выбора категорий из полного списка
    '''
    category = forms.ChoiceField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        category = Category.objects.all()
        choices = [('', 'Все категории')] + [(c.id, c.name) for c in category]
        self.fields['category'].choices = choices
