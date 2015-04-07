# -*- coding: utf-8 -*-

from django import template

from organizations.models import Organization
from organizations.utils import get_users_organizations

register = template.Library()


@register.inclusion_tag('organizations/organization_users.html', takes_context=True)
def organization_users(context, org):
    context.update({'organization_users': org.organization_users.all()})
    return context


@register.assignment_tag
def users_organizations(user):
    """
    Returns all organizations, in wich the user is member.
    Use in Template:
    {% load org_tags %}
    {% users_organizations request.user as my_orgs %}
    """
    if not user or not user.is_authenticated():
        return None
    else:
        return get_users_organizations(user)


@register.assignment_tag
def orgname_for_slug(slug):
    """
    Returns organizations name for a given slug.
    Use in Template:
    {% load org_tags %}
    {% orgname_for_slug request.current_organization %}
    """
    try:
        return Organization.objects.get(slug=slug).name
    except Organization.DoesNotExist:
        return None
