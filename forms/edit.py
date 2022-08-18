from profile.models import User
from profile.forms.base import StyledModelForm


class UserEditForm(StyledModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
