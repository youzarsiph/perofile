from django.urls import reverse_lazy
from profile.views.generic import MessageRequiredDeletionView, RequestUser
from profile.models import User


class UserDeletionView(RequestUser, MessageRequiredDeletionView):
    model = User
    success_url = reverse_lazy('profile:index')
    success_message = 'Account deleted successfully.'
    error_message = 'Error occurred while processing.'
