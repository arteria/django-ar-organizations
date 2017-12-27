# -*- coding: utf-8 -*-
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.http.response import HttpResponseRedirect

from organizations.middleware import OrganizationsMiddleware
from organizations.utils import create_organization

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class VisitorTrackingMiddlewareTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.mw = OrganizationsMiddleware()
        self.factory = RequestFactory()
        self.unknown_user = User.objects.create_user(
            username='anna', email='anna@me.com', password='top_secret'
        )
        self.known_user = User.objects.create_user(
            username='bob', email='bob@me.com', password='top_secret'
        )
        self.org = create_organization(
            self.known_user, 'Test', 'test', is_active=True
        )

    def test_unknown_request_is_redirected(self):
        url = '/admin/'

        request = self.factory.get(url)
        request.user = self.unknown_user
        request.session = {}
        resp = self.mw.process_request(request)

        self.assertEquals(type(resp), HttpResponseRedirect)
        assert reverse('organization_switch') in resp.url

    def test_valid_request_is_passing(self):
        url = '/admin/'

        request = self.factory.get(url)
        request.user = self.known_user
        request.session = {'current_organization': self.org.slug}
        resp = self.mw.process_request(request)

        self.assertEquals(resp, None)
