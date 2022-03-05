
from django.urls import path
from tasks import views

from tasks.views import  taskView, taskViewUpdate, StaskView, StaskViewUpdate, CompletedView, CompletedUpdate, SCompletedView, SCompletedViewUpdate
urlpatterns = [
    path("", views.taskView.as_view()),
    path("<str:pk>/", views.taskViewUpdate.as_view()),
    path('special/', views.StaskView.as_view(),  name='add-comment'),
    path("special/<str:pk>/", views.StaskViewUpdate.as_view()),
    path("completed/", views.CompletedView.as_view()),
    path("completed/<str:pk>/", views.CompletedUpdate.as_view()),
    path("SCompleted/", views.SCompletedView.as_view()),
    path("sCompleted/<str:pk>/", views.SCompletedViewUpdate.as_view()),
    
]