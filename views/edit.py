from django.contrib import messages
from django.urls import reverse_lazy
from profile.views.generic import MessageRequiredEditView, RequestUser
from profile.models import User
from profile.forms.main import UserEditForm


class UserEditView(RequestUser, MessageRequiredEditView):
    model = User
    form_class = UserEditForm
    success_url = reverse_lazy('profile:index')
    success_message = 'Account updated successfully.'
    error_message = 'An error occurred while processing.'

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        if not (user.first_name or user.last_name or user.email):
            messages.success(
                request,
                'Account created successfully, please fill in your information.'
            )
        return super().get(request, *args, **kwargs)
