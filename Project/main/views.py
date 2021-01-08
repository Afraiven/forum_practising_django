from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, Comment
from django.utils import timezone
from .forms import CreateQuestionForm


def comment(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # instead of it you should create new comment !!!!!
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Comment.DoesNotExist):
        # This is OK.
        # Redisplay the question voting form.
        return render(request, 'main/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # This is not ok
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # THANKS FOR SUCH A GREAT ADVICE !!! I was literally looking for this
        return HttpResponseRedirect(reverse('main:results', args=(question.id,)))


def vote(request, question_id):
    # checks if there is an object Question if not it raises 404
    question = get_object_or_404(Question, pk=question_id)
    try:
        # get choice assigned to the question with automatic choice_set made by django <3
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'main/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # THANKS FOR SUCH A GREAT ADVICE !!! I was literally looking for this
        return HttpResponseRedirect(reverse('main:results', args=(question.id,)))


# class index inherits from django.views.generic ListView
class IndexView(generic.ListView):
    template_name = 'main/index.html'
    # name of sth called context object
    context_object_name = 'latest_question_list'

    # func that returns queryset of Questions sorted by publication date
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]


# BOTH ListView and DetailView are predeclared classes from django.views.generic
class DetailView(generic.DetailView):
    # model equals to Question model
    model = Question
    # name of template
    template_name = 'main/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'main/results.html'


def create_question_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateQuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/index/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateQuestionForm()

    return render(request, 'main/create_question.html', {'form': form})
