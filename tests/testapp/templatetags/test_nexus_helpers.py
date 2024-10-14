from bs4 import BeautifulSoup
from django.template import Context, RequestContext, Template
from django.test import RequestFactory, SimpleTestCase

import nexus
from nexus.sites import site


class NexusHelpersTests(SimpleTestCase):
    request_factory = RequestFactory()

    def test_nexus_media_prefix(self):
        out = (
            Template(
                """
            {% load nexus_media_prefix from nexus_helpers %}
            {% nexus_media_prefix %}
        """
            )
            .render(Context())
            .strip()
        )
        assert out == "/nexus/media"

    def test_nexus_version(self):
        out = (
            Template(
                """
            {% load nexus_version from nexus_helpers %}
            {% nexus_version %}
        """
            )
            .render(Context())
            .strip()
        )
        assert out == nexus.__version__

    def test_show_navigation(self):
        request = self.request_factory.get("/")
        out = (
            Template(
                """
            {% load show_navigation from nexus_helpers %}
            {% show_navigation %}
        """
            )
            .render(RequestContext(request, {"nexus_site": site}))
            .strip()
        )
        BeautifulSoup(out, "html.parser")  # checks it is valid HTML
