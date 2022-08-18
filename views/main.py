from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from profile.views.create import *
from profile.views.edit import *
from profile.views.delete import *


# Create your views here.
class IndexView(TemplateView):
    template_name = 'profile/base/index.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/authentication/profile.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/base/dashboard.html'
