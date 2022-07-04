# articles/forms.py
from django import forms

from .models import Comment

# https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/#modelform

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment", "author")
