from django import forms
from .models import Question


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

    class Meta:
        model = Question
        fields = ['question_text', 'question_subtext']
