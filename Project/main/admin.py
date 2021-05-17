from django.contrib import admin
from .models import Question, Comment, Category, Report


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    model = Category


class QuestionAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


class ReportAdmin(admin.ModelAdmin):
    model = Report


admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Report, ReportAdmin)
