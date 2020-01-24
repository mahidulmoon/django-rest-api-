from django.urls import path
#from .views import polls_list, polls_detail
from .apiviews import PollList, PollListgenerics,CreateVote, ChoiceList, UserCreate, LoginView

urlpatterns = [
    #path('polls/',polls_list,name="polls_list"),
    #path("polls/<int:pk>/",polls_detail,name="polls_detail"),
    path('polls/',PollList.as_view(),name="polls_list"),
    #path('polls/',PollListgenerics.as_view(),name="polls_list"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("user/",UserCreate.as_view(),name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]
