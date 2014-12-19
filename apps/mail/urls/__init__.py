from django.conf.urls import patterns, url

from apps.mail.views.website import HomeTemplateView
from apps.mail.views.website import LoginTemplateView
from apps.mail.views.website import RegisterTemplateView
from apps.mail.views.website import LoginUserView
from apps.mail.views.website import LogoutView

urlpatterns = patterns('',
                       url(r'^$',
                           HomeTemplateView.as_view(),
                           name='home'),

                       url(r'^login/$',
                           LoginTemplateView.as_view(),
                           name='login_template_view'),

                       url(r'^register/$',
                           RegisterTemplateView.as_view(),
                           name='register_template_view'),

                       url(r'^post-login/$',
                           LoginUserView.as_view(),
                           name='login'),

                       url(r'^logout/$',
                           LogoutView.as_view(),
                           name='logout'),
                       )