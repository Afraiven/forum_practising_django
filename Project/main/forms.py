from django import forms
from .models import Question, Comment, Category


class CreateQuestionForm(forms.ModelForm):
    question_text = forms.CharField(label='Question',
                                    max_length=200,
                                    widget=forms.TextInput({"placeholder": "Do Androids Dream of Electric Sheep?"})
                                    )
    question_subtext = forms.CharField(label='Question description',
                                       max_length=500,
                                       # Add some nice placeholders
                                       widget=forms.TextInput({"placeholder": ""})
                                       )
    category = forms.ModelMultipleChoiceField(
                                            queryset=Category.objects.all(),
                                            widget=forms.CheckboxSelectMultiple()
                                            )

    class Meta:
        model = Question
        fields = ['question_text', 'question_subtext', 'category']


class CreateCommentForm(forms.ModelForm):
    comment_text = forms.CharField(label='Comment',
                                   max_length=400,
                                   widget=forms.TextInput({"placeholder": "Answer"})
                                   )

    class Meta:
        model = Comment
        fields = ['comment_text']
