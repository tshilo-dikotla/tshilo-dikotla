from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin


class HomeView(EdcBaseViewMixin, NavbarViewMixin, TemplateView):

    template_name = 'tshilo_dikotla/home.html'
    navbar_name = 'tshilo_dikotla'
    navbar_selected_item = 'home'
