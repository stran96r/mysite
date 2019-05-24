from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        ### WIDGETS ###
        widgets = {
            "title": forms.TextInput(attrs={'class':'textinputclass'}),
            "text": forms.Textarea(attrs={'class':'aditable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text')

        ### WIDGETS ###
        widgets = {
            "author": forms.TextInput(attrs={'class':'textinputclass'}),
            "text": forms.Textarea(attrs={'class':'aditable medium-editor-textarea'})
        }