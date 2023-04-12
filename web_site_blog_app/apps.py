from django.apps import AppConfig


class WebSiteBlogAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web_site_blog_app'

    def ready(self):
        import web_site_blog_app.signals