from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(sef):
        import blog.signals
