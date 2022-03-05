
from django.urls import path
from tasks.views import taskView, taskViewUpdate, StaskView, StaskViewUpdate, CompletedView, CompletedUpdate, SCompletedView, SCompletedViewUpdate

urlpatterns = [
    path("", taskView.as_view()),
    path("special/", StaskView.as_view()),
    path("special/<str:pk>/", StaskViewUpdate.as_view()),
    path("completed/", CompletedView.as_view()),
    path("completed/<str:pk>/", CompletedUpdate.as_view()),
    path("SCompleted/", SCompletedView.as_view()),
    path("sCompleted/<str:pk>/", SCompletedViewUpdate.as_view()),
    path("<str:pk>/", taskViewUpdate.as_view()),
    
]