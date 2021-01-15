from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

from .models import Choice, Question
from .forms import CreateQuestionForm, CreateCommentForm


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
class DetailView(generic.FormView, generic.DetailView):
    # model equals to Question model
    form_class = CreateCommentForm
    template_name = 'main/detail.html'

    def get_success_url(self):
        return reverse('main:detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        # self.success_url = reverse(str())
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form_obj = form.save(commit=False)
        form_obj.user = self.request.user
        form_obj.question = Question.objects.get(pk=self.kwargs['pk'])
        form_obj.pub_date = timezone.now()

        messages.success(self.request, "Answer posted")
        form_obj.save()
        return super().form_valid(form)

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'main/results.html'


@login_required(login_url="/login/")
def create_question_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateQuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.pub_date = timezone.now()

            messages.success(request, "Your question has been added successfully")
            form_obj.save()
            return HttpResponseRedirect(reverse('main:index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateQuestionForm()

    return render(request, 'main/create_question.html', {'form': form})
