from django.contrib import admin
from .models import Question, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Question, QuestionAdmin)
