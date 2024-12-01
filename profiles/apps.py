from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import profiles.signals  # Ensure signals are imported when the app is ready

