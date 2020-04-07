from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(sef):
        import users.signals
