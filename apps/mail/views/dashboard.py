from django.views.generic import TemplateView


class dashboardTemplate(TemplateView):
    template_name = 'dashboard.html'