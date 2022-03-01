from django.urls import path
from django.urls.resolvers import URLPattern
from home import views
from home.views import HomePageView,TeamPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("team/", TeamPageView.as_view(), name="team"),
]