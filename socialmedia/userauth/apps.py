from django.apps import AppConfig


class UserauthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userauth'

    def ready(self):
        print("ready method called")
        from userauth.schedule import scheduler
        scheduler.start()