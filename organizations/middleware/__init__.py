# -*- coding: utf-8 -*-
from django.shortcuts import redirect

from organizations.models import Organization
from organizations.utils import set_current_organization_to_session, get_current_organization, skip_request

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    class MiddlewareMixin(object):
        pass


class OrganizationsMiddleware(MiddlewareMixin):
    """
    Simple Middleware that redirects all request to the switch_org view
    if no current_organization is stored in request.session

    Skip the redirect by providing '?org=<slug>' as get parameter
    """
    def process_request(self, request):

        if skip_request(request):
            return None

        org_slug = request.GET.get('org')
        if org_slug:
            try:
                orgs = Organization.objects.get_for_user(request.user)
                org = orgs.get(slug=org_slug)
            except Organization.DoesNotExist:
                org = None
            except Organization.MultipleObjectsReturned:
                org = None
            if org:
                set_current_organization_to_session(request, org)

        current_organization = get_current_organization(request)

        if callable(request.user.is_authenticated):
            is_authenticated = request.user.is_authenticated()
        else:
            is_authenticated = request.user.is_authenticated

        if not request.path == reverse('organization_switch') and not current_organization and is_authenticated:
            # skip the redirect and set current_organization if user is member of only one Organization
            url = reverse('organization_switch')
            url += "?next=%s" % request.path
            return redirect(url)

        return None
