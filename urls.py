from django.urls import path
from django.contrib.auth import views
from django.views.generic import RedirectView
from profile.forms.main import *
from profile.views.main import *
from django.urls import reverse_lazy

# To change the app name.
app_name = 'profile'
urlpatterns = [
    # Main Views
    path(
        '',
        IndexView.as_view(),
        name='home'
    ),
    path(
        'dashboard/',
        DashboardView.as_view(),
        name='dashboard'
    ),

    # Profile
    path(
        'accounts/',
        RedirectView.as_view(pattern_name='profile:index'),
        name='redirect'
    ),
    path(
        'accounts/profile/',
        ProfileView.as_view(),
        name='index'
    ),

    # Authentication
    path(
        'accounts/login/',
        views.LoginView.as_view(
            form_class=StyledAuthenticationForm,
            template_name='profile/authentication/login.html',
            extra_context={
                'signup_form': StyledUserCreationForm()
            }
        ),
        name='login'
    ),
    path(
        'accounts/register/',
        UserCreationView.as_view(),
        name='register'
    ),
    path(
        'accounts/<int:id>/edit/',
        UserEditView.as_view(),
        name='edit_user'
    ),
    path(
        'accounts/<int:id>/delete/',
        UserDeletionView.as_view(),
        name='delete_user'
    ),
    path(
        'accounts/logout/',
        views.LogoutView.as_view(
            template_name='profile/authentication/logged_out.html'
        ),
        name='logout'
    ),

    # Password
    path(
        'accounts/password/change/',
        views.PasswordChangeView.as_view(
            form_class=StyledPasswordChangeForm,
            template_name='profile/authentication/change_password.html',
            success_url=reverse_lazy('profile:change_done')
        ),
        name='change_password'
    ),
    path(
        'accounts/password/change/done/',
        views.PasswordChangeDoneView.as_view(
            template_name='profile/authentication/change_done.html'
        ),
        name='change_done'
    ),
    path(
        'accounts/password/reset/',
        views.PasswordResetView.as_view(
            form_class=StyledPasswordResetForm,
            template_name='profile/authentication/reset_password.html',
            success_url=reverse_lazy('profile:reset_done')
        ),
        name='reset_password'
    ),
    path(
        'accounts/password/reset/done/',
        views.PasswordResetDoneView.as_view(
            template_name='profile/authentication/reset_done.html'
        ),
        name='reset_done'
    ),
    path(
        'accounts/password/reset/confirm/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(
            template_name='profile/authentication/reset_confirm.html',
            form_class=StyledPasswordResetForm,
            success_url=reverse_lazy('profile:reset_complete')
        ),
        name='reset_confirm'
    ),
    path(
        'accounts/password/reset/complete/',
        views.PasswordResetCompleteView.as_view(
            template_name='profile/authentication/reset_complete.html',
        ),
        name='reset_complete'
    ),
]
