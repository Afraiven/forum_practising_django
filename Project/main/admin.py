from django.contrib import admin
from .models import Question, Choice, Comment


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, CommentInline]


admin.site.register(Question, QuestionAdmin)
