from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class MessageMixin:
    """
    Base mixin class to add success and error messages.
    """
    success_message = str()
    error_message = str()


class MessageMixinCreateView(MessageMixin):
    """
    A mixin for CreateView to set success and error messages.
    """

    def post(self, request, *args, **kwargs):
        try:
            response = super(MessageMixinCreateView, self).post(
                request, *args, **kwargs)
            messages.success(request, self.success_message)
            return response
        except Exception:
            messages.error(request, self.error_message)
            return redirect(request.path)


class MessageMixinUpdateView(MessageMixin):
    """
    A mixin for UpdateView to set success and error messages.
    """

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, self.success_message)
        return super().post(request, *args, **kwargs)


class MessageMixinDeleteView(MessageMixin):
    """
    A mixin for DeleteView to set success and error messages.
    """

    def post(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return self.delete(request, *args, **kwargs)


class RequestUser(UserPassesTestMixin):
    """
    A mixin for UpdateView, DeleteView and DetailView to limit the user to only modifying or viewing their
    own user object. In other words, the current logged in user can edit their account only.
    """

    def test_func(self):
        return self.request.user == self.get_object()


class TemplateNameMixin:
    """
    A mixin to set the template_name and it's extension.
    """
    app_name = 'profile'
    parent_dir = ''
    extension = ''

    def get_template_names(self):
        template = self.app_name + '/views/' + self.parent_dir + \
            self.model._meta.verbose_name.title().lower()
        template += self.extension
        return [template]
