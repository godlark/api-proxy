from django.apps import AppConfig


class CallbacksConfig(AppConfig):

    name = "proxy_api.callbacks"
    verbose_name = "Callbacks"

    def ready(self):
        pass
