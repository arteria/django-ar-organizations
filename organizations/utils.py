# -*- coding: utf-8 -*-

from django.conf import settings

from organizations.models import Organization, OrganizationUser, OrganizationOwner
from compat import get_user_model

User = get_user_model()


def create_organization(user, name, slug, is_active=True):
    """
    Returns a new organization, also creating an initial organization user who
    is the owner.
    """
    organization = Organization.objects.create(name=name, slug=slug, is_active=is_active)
    new_user = OrganizationUser.objects.create(organization=organization, user=user, is_admin=True)
    OrganizationOwner.objects.create(organization=organization, organization_user=new_user)

    return organization


def model_field_attr(model, model_field, attr):
    """
    Returns the specified attribute for the specified field on the model class.
    """
    fields = dict([(field.name, field) for field in model._meta.fields])
    try:
        return getattr(fields[model_field], attr)
    except Exception as ex:
        return "ERROR " + str(ex)


def set_current_organization_to_session(request, org):
    """
    Sets the current org in request.session
    """
    if request.session.get('current_organization', None) is not None:  # current_org already in session
        if request.session['current_organization'] == org.slug:  # same values, no need to update
            request.session['current_organization_modified'] = False
            request.session.modified = True
            return
    # current_org not in session or not same values
    request.session['current_organization'] = org.slug
    request.session['current_organization_modified'] = True
    request.session.modified = True
    return


def get_current_organization(request):
    """
    Retuns the current organization object if set in the session or
    user is member in only one orzanization.
    None if not multi client app.
    """
    multi_client = getattr(settings, 'AR_CRM_MULTI_CLIENT', True)
    if not multi_client:
        return None

    current_org_slug = request.session.get('current_organization')
    if request.user.is_authenticated():
        try:
            org = Organization.objects.get(users=request.user, slug=current_org_slug)
        except Organization.DoesNotExist:
            org = None
            orgs = Organization.objects.filter(users=request.user)
            if orgs.count() == 1:  # user is member of one organization
                org = orgs[0]
                set_current_organization_to_session(request, org)
    else:
        org = None

    return org


def get_users_organizations(user):
    """
    Return a list of organizations for a given user
    """
    if not user or not user.is_active or not user.is_authenticated():
        return None
    return Organization.objects.get_for_user(user).all()


def get_organization_members(organization):
    """
    returns a list of OrganizationUsers for given organization
    """
    return OrganizationUser.objects.filter(organization=organization)


def get_organization_users(organization):
    """
    Returns a list of Users for a given organization
    """
    organization_users = OrganizationUser.objects.filter(organization=organization)
    user_pk_list = []
    for organization_user in organization_users:
        user_pk_list.append(organization_user.user.pk)

    return User.objects.filter(pk__in=user_pk_list)
