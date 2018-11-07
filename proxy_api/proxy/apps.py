from django.apps import AppConfig


class ProxyConfig(AppConfig):

    name = "proxy_api.proxy"
    verbose_name = "Proxy"

    def ready(self):
        pass
