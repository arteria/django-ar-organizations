from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


from organizations.models import Organization
from organizations.utils import set_current_organization_to_session, get_current_organization


class OrganizationsMiddleware:
    """
    Simple Middleware thas updates the current org in the session
    if 'org' was passed in the GET query string.
    """

    def process_request(self, request):
        AR_CRM_MULTI_CLIENT = getattr(settings, 'AR_CRM_MULTI_CLIENT', False)
        if not AR_CRM_MULTI_CLIENT:
            return None

        org_slug = request.GET.get('org')
        if org_slug:
            try:
                org = Organization.objects.get_for_user(request.user).get(slug=org_slug)
            except ObjectDoesNotExist:
                org = None

            if org:
                set_current_organization_to_session(request, org)

        current_organization = get_current_organization(request)
        if not request.path == reverse('organization_switch') and not current_organization and request.user.is_authenticated():
            url = reverse('organization_switch')
            url += "?next=%s" % request.path
            return redirect(url)

        return None
