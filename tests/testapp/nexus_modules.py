import multiprocessing
import platform

from django.urls import path

import nexus


class HelloWorldModule(nexus.NexusModule):
    home_url = 'index'
    name = 'hello-world'

    def get_title(self):
        return 'Hello World'

    def get_urls(self):
        return [
            path('', self.as_view(self.index), name='index'),
        ]

    def render_on_dashboard(self, request):
        return self.render_to_string('nexus/example/dashboard.html', {
            'title': 'Hello World',
        })

    def index(self, request):
        return self.render_to_response("nexus/example/index.html", {
            'title': 'Hello World',
        }, request)


nexus.site.register(HelloWorldModule, 'hello-world')

# optionally you may specify a category
# nexus.site.register(HelloWorldModule, 'hello-world', category='cache')


class SystemStatsModule(nexus.NexusModule):
    """
    Modules don't need to have URLs, they can just appear on the dashboard -
    simply don't name `home_url` or implement `get_urls()`.
    """
    name = 'system-stats'

    def get_title(self):
        return 'System Stats'

    def render_on_dashboard(self, request):
        return self.render_to_string('nexus/system-stats/dashboard.html', {
            'stats': {
                'num_cpus': multiprocessing.cpu_count(),
                'platform': platform,
            },
        })


nexus.site.register(SystemStatsModule, 'system-stats')


class StyleGuideModule(nexus.NexusModule):
    """
    Modules can also not appear on the dashboard, but not implementing
    render_on_dashboard, and only have URLs.
    """
    home_url = 'index'
    name = 'style-guide'

    def get_title(self):
        return 'Style Guide'

    def get_urls(self):
        return [
            path('', self.as_view(self.index), name='index'),
        ]

    def index(self, request):
        return self.render_to_response('nexus/styleguide/index.html', {
            'title': 'Style Guide',
        }, request)


nexus.site.register(StyleGuideModule, 'style-guide')
