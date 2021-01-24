from django.contrib import admin
from .models import Question, Comment, Category


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    model = Category


class QuestionAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
