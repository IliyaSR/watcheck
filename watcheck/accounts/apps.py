from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'watcheck.accounts'

    def ready(self):
        import watcheck.accounts.signals
        result = super().ready()
        return result
