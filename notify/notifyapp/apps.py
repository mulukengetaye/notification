from django.apps import AppConfig


class NotifyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifyapp'
    # 1. 👇 Add this line for signals
    def ready(self):
        import notifyapp.signals