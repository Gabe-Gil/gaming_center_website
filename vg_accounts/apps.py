from django.apps import AppConfig


class VgAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vg_accounts'

    def ready(self):
        import vg_accounts.signals
