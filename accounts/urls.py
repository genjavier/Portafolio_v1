from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import (
    login, logout
)
app_name = 'accounts'
urlpatterns = [
    # path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    # path('logout/', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/<int:pk>/', views.view_profile, name='view_profile_with_pk'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),

    # path('reset-password/', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),

    # path('reset-password/done/', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),

    # # path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),

    # path('reset-password/complete/', password_reset_complete,{'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete')

]
