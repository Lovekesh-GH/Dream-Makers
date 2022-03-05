from django.shortcuts import render
from django.views.generic import TemplateView
# from webpush.utils import send_to_subscription
# # from django.
# from user.models import Users


# Create your views here.

# def HomePageView(request):
#     # webpush = {"group": group_name }
#     payload = {"head": "Welcome!", "body": "Hello World"}

    
#     users = Users.objects.all()
#     push_infos = users.webpush_info.select_related("subscription")
#     for push_info in push_infos:
#         send_to_subscription(push_info.subscription, payload)
#     return render(request, 'home.html',  {"payload":payload})
    # template_name = "home.html"

class HomePageView(TemplateView):
    template_name = "home.html"

class TeamPageView(TemplateView):
    template_name = "team.html"

