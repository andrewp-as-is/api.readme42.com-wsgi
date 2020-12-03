from django.urls import path
from django.conf.urls import include

from views.templates import TemplateView

urlpatterns = [
    path('<str:login>/<slug:slug>', TemplateView.as_view()),
]
