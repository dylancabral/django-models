from django.views.generic import TemplateView


class HomePAgeView(TemplateView):
    template_name = 'home.html'
