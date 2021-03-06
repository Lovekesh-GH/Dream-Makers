from django.urls import path

from .views import UserView, UsersView, userPresentOrNot

urlpatterns = [
    path("", UsersView.as_view()),
    path("<str:pk>/", UserView.as_view()),
    path("checkUser/<str:email>", userPresentOrNot)
]