from django import forms
from .models import Quiz, Question, Option
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'amount']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'set']

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['name', 'question', 'correct']
