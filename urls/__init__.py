from django.urls import path
from django.conf.urls import include

import views

urlpatterns = [
    path('templates/', include('urls.templates.urls')),
    path('', views.IndexView.as_view()),
]
