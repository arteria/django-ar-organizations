from django.core.exceptions import ObjectDoesNotExist
from organizations.models import Organization
from organizations.utils import set_current_organization_to_session


class OrganizationsMiddleware:
    """
    Simple Middleware thas updates the current org in the session
    if 'org' was passed in the GET query string.
    """

    def process_request(self, request):
        org_slug = request.GET.get('org')
        if org_slug:
            try:
                org = Organization.objects.get_for_user(request.user).get(slug=org_slug)
            except ObjectDoesNotExist:
                print "no matching org"
                org = None

            if org:
                set_current_organization_to_session(request, org)

        return None
