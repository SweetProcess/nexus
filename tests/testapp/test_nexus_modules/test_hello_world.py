from django.contrib.auth.models import User
from django.test import TestCase


class HelloWorldModuleTests(TestCase):
    def setUp(self):
        self.user = User(username="user", is_staff=True)
        self.user.set_password("password")
        self.user.save()
        self.client.login(username="user", password="password")

    def test_is_on_dashboard(self):
        resp = self.client.get("/nexus/")
        assert resp.status_code == 200
        assert "Hello World" in resp.content.decode("utf-8")

    def test_index_page(self):
        resp = self.client.get("/nexus/hello-world/")
        assert resp.status_code == 200
        assert "Hello World" in resp.content.decode("utf-8")
