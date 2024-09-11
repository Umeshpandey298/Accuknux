from django.apps import AppConfig


class SynchDjangoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'synch_Django'

    def ready(self):
        import synch_Django.signals 
    

