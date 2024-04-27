from django.apps import AppConfig


class SarzappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sarzapp'

    def ready(self):
    	import sarzapp.signals
