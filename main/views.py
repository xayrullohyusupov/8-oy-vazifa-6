from django.shortcuts import render, redirect
from .forms import QuizForm
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm,QuestionForm
from django.contrib.auth.forms import AuthenticationForm
from . import models


def home(request):
    quizzes = models.Quiz.objects.all() 
    context = {
        'quizzes': quizzes
    }
    return render(request, 'index.html', context)

def quiz_detail(request, pk):
    quiz = get_object_or_404(models.Quiz, id=pk)
    questions = quiz.questions.all()
    context = {
        'quiz': quiz,
        'questions': questions
    }
    return render(request, 'quiz_detail.html', context)

@login_required
def create_quiz(request):
    if request.method == 'POST':
        quiz_form = QuizForm(request.POST)
        if quiz_form.is_valid():
            quiz = quiz_form.save(commit=False)
            quiz.author = request.user
            quiz.save()
            return redirect('home')  
    else:
        quiz_form = QuizForm()
    return render(request, 'create_quiz.html', {'form': quiz_form})

def create_question(request, quiz_id):
    quiz = get_object_or_404(models.Quiz, pk=quiz_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.set = models.QuestionSet.objects.get(quiz=quiz)
            question.save()
            return redirect('quiz_detail', pk=quiz.id)
    else:
        form = QuestionForm()
    return render(request, 'create_question.html', {'form': form, 'quiz': quiz})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'profile.html')