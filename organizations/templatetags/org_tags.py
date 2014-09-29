from django import template

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
