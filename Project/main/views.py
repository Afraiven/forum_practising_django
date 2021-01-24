from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

from .models import Question, VoterUp, VoterDown, Comment, Category
from .forms import CreateQuestionForm, CreateCommentForm


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    question_id = comment.question.id
    comment.delete()

    return HttpResponseRedirect(reverse('main:detail', args=(question_id,)))


def vote_up(request, question_id):
    if VoterUp.objects.filter(question_id=question_id, user_id=request.user.id).exists():
        question = get_object_or_404(Question, pk=question_id)
        question.votes -= 1
        question.save()
        v = VoterUp.objects.filter(user=request.user).all()
        v.delete()

    else:
        messages.success(request, "Voted Up")
        question = get_object_or_404(Question, pk=question_id)
        question.votes += 1
        v = VoterUp(user=request.user, question=question)
        v.save()
        if VoterDown.objects.filter(question_id=question_id, user_id=request.user.id).exists():
            v = VoterDown.objects.filter(user=request.user).all()
            v.delete()
            question.votes += 1
        question.save()

    return HttpResponseRedirect(reverse('main:detail', args=(question_id,)))


def vote_down(request, question_id):
    if VoterDown.objects.filter(question_id=question_id, user_id=request.user.id).exists():
        question = get_object_or_404(Question, pk=question_id)
        question.votes += 1
        question.save()
        v = VoterDown.objects.filter(user=request.user).all()
        v.delete()
    else:
        messages.warning(request, "Voted Down")
        question = get_object_or_404(Question, pk=question_id)
        question.votes -= 1
        v = VoterDown(user=request.user, question=question)
        v.save()
        if VoterUp.objects.filter(question_id=question_id, user_id=request.user.id).exists():
            v = VoterUp.objects.filter(user=request.user).all()
            v.delete()
            question.votes -= 1
        question.save()

    return HttpResponseRedirect(reverse('main:detail', args=(question_id,)))


class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'latest_question_list'
    paginate_by = 8

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class DetailView(generic.FormView, generic.DetailView):
    form_class = CreateCommentForm
    template_name = 'main/detail.html'

    def get_success_url(self):
        return reverse('main:detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form_obj = form.save(commit=False)
        form_obj.user = self.request.user
        form_obj.question = Question.objects.get(pk=self.kwargs['pk'])
        form_obj.pub_date = timezone.now()

        messages.success(self.request, "Answer posted")
        form_obj.save()
        return super().form_valid(form)

    def get_queryset(self):
        try:
            messages.info(self.request, str(VoterUp.objects.filter(user=self.request.user).count()-VoterDown.objects.filter(user=self.request.user).count()))
        except:
            pass
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


@login_required(login_url="/login/")
def create_question_view(request):
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.pub_date = timezone.now()

            messages.success(request, "Your question has been added successfully")
            form_obj.save()
            return HttpResponseRedirect(reverse('main:index'))

    else:
        form = CreateQuestionForm()

    return render(request, 'main/create_question.html', {'form': form})


class RankingView(generic.ListView):
    template_name = 'main/ranking.html'
    context_object_name = 'latest_question_list'
    paginate_by = 10

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-votes')[:10]


class CategoryView(generic.ListView):
    template_name = 'main/category.html'
    context_object_name = 'cat'

    def get_queryset(self):
        cat = Category.objects.all()
        return cat


class CategoryIndexView(generic.ListView):
    template_name = 'main/category_index.html'
    context_object_name = 'category_index'
    paginate_by = 8

    def get_queryset(self):
        cat = Category.objects.get(name=self.kwargs['category'])
        return (Question.objects.filter(
            category=cat
        ).order_by('-pub_date'), cat)

