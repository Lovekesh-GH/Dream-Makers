from django.contrib import admin
from django.urls import path,include
from django.urls import re_path as url

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path('Notification/', include('Notification.urls')),
    path('user/', include('user.urls')),
    path('tasks/', include('tasks.urls')),
    url(r'^webpush/', include('webpush.urls'))
]
