from django.urls import reverse_lazy
from profile.views.generic import CreationView
from profile.models import User
from profile.forms.create import UserCreationForm


class UserCreationView(CreationView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('profile:login')

    def get_success_url(self):
        return reverse_lazy('profile:edit_user', args=[self.object.pk])
