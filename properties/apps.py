from django.apps import AppConfig

class PropertiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'properties'

    def ready(self):
        # Importing signals inside ready() ensures they are registered 
        # as soon as the app registry is fully populated.
        import properties.signals