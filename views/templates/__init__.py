from django.http import HttpResponse
from django.views.generic.base import View
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from apps.core.token.models import Token

class TemplateView(View):
    def dispatch(self, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' not in self.request.META:
            return HttpResponse('Unauthorized', status=401)
        try:
            value = self.request.META['HTTP_AUTHORIZATION'].replace('Token ','')
            token = Token.objects.get(value=value)
            self.github_user = token.created_by
            return super(TemplateView, self).dispatch(*args, **kwargs)
        except Token.DoesNotExist:
            return HttpResponse('Unauthorized', status=401)

    def post(self, request, login, slug):
        context = {'username':self.github_user.login,'template':slug}
        for key, value in request.headers.items():
            if 'readme42-' in key.lower():
                name = '-'.join(key.split('-')[1:]).lower()
                context[name] = mark_safe(value)
        for basename,f in request.FILES.items():
            name = basename.split('.')[0].lower()
            value = mark_safe(f.read().decode("utf-8"))
            context[name] = value
        for k in request.POST.keys():
            context[k] = mark_safe(request.POST.get(k))
        template_name = '%s/%s' % (login,slug)
        out = render_to_string(template_name,context=context).strip()
        while '\n\n\n#' in out:
            out = out.replace('\n\n\n#','\n\n#')
        while '\n\n\n<' in out:
            out = out.replace('\n\n\n<','\n\n<')
        return HttpResponse(out, content_type="text/plain")


# https://postmarkapp.com/developer/api/overview
# 401 — Unauthorized Missing or incorrect API token in header.
