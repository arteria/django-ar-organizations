# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from compat import url

from organizations import views


urlpatterns = [
    # Organization URLs
    url(r'^$', view=login_required(views.OrganizationList.as_view()),
        name="organization_list"),
    url(r'^switch/$', view=views.switch_org,
        name="organization_switch"),
    url(r'^add/$', view=login_required(views.OrganizationCreate.as_view()),
        name="organization_add"),
    url(r'^(?P<organization_pk>[\d]+)/$',
        view=login_required(views.OrganizationDetail.as_view()),
        name="organization_detail"),
    url(r'^(?P<organization_pk>[\d]+)/edit/$',
        view=login_required(views.OrganizationUpdate.as_view()),
        name="organization_edit"),
    url(r'^(?P<organization_pk>[\d]+)/delete/$',
        view=login_required(views.OrganizationDelete.as_view()),
        name="organization_delete"),

    # Organization user URLs
    url(r'^(?P<organization_pk>[\d]+)/people/$',
        view=login_required(views.OrganizationUserList.as_view()),
        name="organization_user_list"),
    url(r'^(?P<organization_pk>[\d]+)/people/add/$',
        view=login_required(views.OrganizationUserCreate.as_view()),
        name="organization_user_add"),
    url(r'^(?P<organization_pk>[\d]+)/people/(?P<user_pk>[\d]+)/remind/$',
        view=login_required(views.OrganizationUserRemind.as_view()),
        name="organization_user_remind"),
    url(r'^(?P<organization_pk>[\d]+)/people/(?P<user_pk>[\d]+)/$',
        view=login_required(views.OrganizationUserDetail.as_view()),
        name="organization_user_detail"),
    url(r'^(?P<organization_pk>[\d]+)/people/(?P<user_pk>[\d]+)/edit/$',
        view=login_required(views.OrganizationUserUpdate.as_view()),
        name="organization_user_edit"),
    url(r'^(?P<organization_pk>[\d]+)/people/(?P<user_pk>[\d]+)/delete/$',
        view=login_required(views.OrganizationUserDelete.as_view()),
        name="organization_user_delete"),
]
