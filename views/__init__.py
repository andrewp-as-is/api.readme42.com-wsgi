from django.contrib.auth import logout
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.http import HttpResponse
from django.shortcuts import redirect

from django.views.generic.base import View, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, FormView, UpdateView
from django.template import Template, Context
from django.utils.safestring import mark_safe


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('42', content_type="text/plain")
