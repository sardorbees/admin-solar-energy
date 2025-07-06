from django.apps import AppConfig

class DarkplanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'darkplan'

def ready(self):
    import darkplan.signals