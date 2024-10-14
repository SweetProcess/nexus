from django.urls import include, path, re_path
from django.contrib import admin

import nexus

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    path("nexus/", include(nexus.site.urls)),
]
