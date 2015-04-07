# -*- coding: utf-8 -*-

import django
from django.db import models


class OrgManager(models.Manager):

    def get_for_user(self, user):
        if django.VERSION < (1, 7):
            return self.get_query_set().filter(users=user)
        else:
            return self.get_queryset().filter(users=user)


class ActiveOrgManager(OrgManager):
    """
    A more useful extension of the default manager which returns querysets
    including only active organizations
    """

    def get_queryset(self):
        super_ = super(ActiveOrgManager, self)
        if django.VERSION < (1, 7):
            qs = super_.get_query_set()
        else:
            qs = super_.get_queryset()

        return qs.filter(is_active=True)

    if django.VERSION < (1, 7):
        get_query_set = get_queryset
