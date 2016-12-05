# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import user_passes_test, REDIRECT_FIELD_NAME
from organizations.models import OrganizationUser


def organizations_member_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in if the current user is a member of an organisation,
    redirecting to the log-in page if necessary.
    """

    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated() and bool(OrganizationUser.objects.filter(user=u).count()),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def organizations_admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in if the current user is a member of an organisation with admin rights,
    redirecting to the log-in page if necessary.
    """

    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated() and bool(OrganizationUser.objects.filter(user=u, is_admin=True).count()),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
