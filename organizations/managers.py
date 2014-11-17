import django
from django.db import models


class OrgManager(models.Manager):

    def get_for_user(self, user):
        return self.get_queryset().filter(users=user)


class ActiveOrgManager(OrgManager):
    """
    A more useful extension of the default manager which returns querysets
    including only active organizations
    """

    def get_queryset(self):
        return super(ActiveOrgManager,
                self).get_queryset().filter(is_active=True)

    if django.VERSION < (1, 6):
        get_query_set = get_queryset
