from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/voteup/', views.vote_up, name='vote_up'),
    path('<int:question_id>/votedown/', views.vote_down, name='vote_down'),
    path('create_question/', views.create_question_view, name='create_question'),
]
