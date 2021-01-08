from django import forms
from django.utils import timezone


class CreateQuestionForm(forms.Form):
    question_text = forms.CharField(label='Question',
                                    max_length=200,
                                    widget=forms.TextInput({"placeholder": "Do Androids Dream of Electric Sheep?"})
                                    )
    question_subtext = forms.CharField(label='Question description',
                                       max_length=500,
                                       # Add some nice placeholders
                                       widget=forms.TextInput({"placeholder": ""})
                                       )
    pub_date = timezone.now()
