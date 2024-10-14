from django.test import SimpleTestCase
from django.test.utils import override_settings

from nexus.conf import nexus_settings


class NexusSettingsTests(SimpleTestCase):
    @override_settings(NEXUS_MEDIA_PREFIX="/mynexusprefix/")
    def test_with_override_settings(self):
        assert nexus_settings.MEDIA_PREFIX == "/mynexusprefix/"

    @override_settings(
        NEXUS_USE_DJANGO_MEDIA_URL=True,
        MEDIA_URL="/a-big-test/",
    )
    def test_use_django_media_url(self):
        assert nexus_settings.MEDIA_PREFIX == "/a-big-test/"
