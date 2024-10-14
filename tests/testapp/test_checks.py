from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings

from nexus.checks import check_requirements

INSTALLED_APPS_WITHOUT_AUTH = list(
    set(settings.INSTALLED_APPS) - {"django.contrib.auth"}
)


class ChecksTests(TestCase):
    def test_requirements_pass(self):
        assert check_requirements([]) == []

    @override_settings(INSTALLED_APPS=INSTALLED_APPS_WITHOUT_AUTH)
    def test_requirements_fail(self):
        assert len(check_requirements([])) == 1

    @override_settings(
        NEXUS_SKIP_INSTALLED_APPS_REQUIREMENTS=True,
        INSTALLED_APPS=INSTALLED_APPS_WITHOUT_AUTH,
    )
    def test_requirements_fail_suppressed(self):
        assert check_requirements([]) == []
