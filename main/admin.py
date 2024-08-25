from django.contrib import admin
from .models import Quiz, QuestionSet, Question, Option, Answer, AnswerDetail

class OptionInline(admin.TabularInline):
    model = Option
    extra = 3

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2

class QuestionSetInline(admin.TabularInline):
    model = QuestionSet
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'amount')
    inlines = [QuestionSetInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'set')
    inlines = [OptionInline]

class OptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'question', 'correct')

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Answer)
admin.site.register(AnswerDetail)
admin.site.register(QuestionSet)
